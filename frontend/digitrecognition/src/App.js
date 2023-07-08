import React, { useState } from "react";
import { DrawingArea } from "./DrawingArea/DrawingArea";
import "./App.css";

export default function App() {

  return (
    <div
      className="App"
    >
      <h1 className="title">Draw a digit!</h1>
      <svg width="400px" height="400px">
        <DrawingArea x={0} y={0} width={400} height={400} />
      </svg>
    </div>
  );
}
