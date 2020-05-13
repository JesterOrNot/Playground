import React from "react";
import ReactDOM from "react-dom";

export default function MediaCard({ title, body, imageUrl }) {
  return (
    <div className="MediaCard">
      <img src={imageUrl} />
      <div className="MediaCardText">
        <h2>{title}</h2>
        <p>{body}</p>
      </div>
    </div>
  );
}
