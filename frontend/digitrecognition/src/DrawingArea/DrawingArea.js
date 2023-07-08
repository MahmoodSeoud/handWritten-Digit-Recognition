import React, {
    useMemo,
    useState,
    useRef,
    useEffect,
    useCallback
} from "react";
import * as d3 from "d3";
import axios from "axios";


const Line = ({ points }) => {
    const line = useMemo(() => {
        return d3
            .line()
            .x((d) => d.x)
            .y((d) => d.y)
            .curve(d3.curveBasisOpen);
    }, []);


    return (
        <path
            d={line(points)}
            style={{
                stroke: "#F28C28",
                strokeWidth: 2,
                strokeLinejoin: "round",
                strokeLinecap: "round",
                fill: "none"
            }}
        />
    );
};

export const DrawingArea = ({ x, y, width, height }) => {
    const [drawing, setDrawing] = useState(false);
    const [currentLine, setCurrentLine] = useState({ points: [] });
    const [lines, setLines] = useState([]);

    const drawingAreaRef = useRef();


    const mouseMove = useCallback(
        function (event) {
            const [x, y] = d3.pointer(event);
            if (drawing) {
                setCurrentLine((line) => ({
                    ...line,
                    points: [...line.points, { x, y }]
                }));
            }
        },
        [drawing]
    );


    function enableDrawing() {
        setCurrentLine({ points: [] });
        setDrawing(true);
    }


    function disableDrawing() {
        setDrawing(false);
        setLines((lines) => [...lines, currentLine]);
    }


    function resetDrawing() {
        setLines([]);
        setCurrentLine({ points: [] });
        setDrawing(false);
    }


    useEffect(() => {
        const area = d3.select(drawingAreaRef.current);
        area.on("mousemove", mouseMove);
        return () => area.on("mousemove", null);
    }, [mouseMove]);


    async function captureDrawing() {
        const svgElement = drawingAreaRef.current;
        const svgData = new XMLSerializer().serializeToString(svgElement);
        const dataURL = `data:image/svg+xml;base64,${btoa(svgData)}`; // Capture the drawn image as a data URL    

        console.log(dataURL);
        debugger

        try {
            const response = await axios.post('http://localhost:5000/api/process-image', { image: dataURL });
            console.log(response);
        }
        catch (e) {
            console.error(e);
        }
    }





    return (
        <>
            <g
                transform={`translate(${x}, ${y})`}
                ref={drawingAreaRef}
                onMouseDown={enableDrawing}
                onMouseUp={disableDrawing}
            >
                <rect
                    x={0}
                    y={0}
                    width={width}
                    height={height}
                    style={{ fill: "#232b2b" }}
                />
                {lines.map((line, i) => (
                    <Line points={line.points} key={i} />
                ))}
                <Line points={currentLine.points} />

            </g>

            <svg>
                <rect
                    x={10}
                    y={10}
                    style={{ fill: "gray" }}
                    onClick={resetDrawing}
                    width={50}
                    height={20}
                    rx={5}
                    ry={5}
                />
                <text
                    x={20}
                    y={25}
                    fontSize={12}
                    fill="white"
                    onClick={resetDrawing}
                >
                    Reset
                </text>
            </svg>

            <svg>
                <rect
                    x={64}
                    y={64}
                    style={{ fill: "gray" }}
                    onClick={captureDrawing}
                    width={50}
                    height={20}
                    rx={5}
                    ry={5}
                />
                <text
                    x={74}
                    y={79}
                    fontSize={12}
                    fill="white"
                    onClick={captureDrawing}
                >
                    Save
                </text>
            </svg>
        </>
    );
};
