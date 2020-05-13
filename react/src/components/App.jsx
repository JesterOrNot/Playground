import React from "react";
import ReactDOM from "react-dom";
import Hi from "./Hello";
import MediaCard from "./MediaCard";

export default function App() {
  return (
    <div>
      <div className="cards">
        <MediaCard
          title="GitHub"
          style={{ display: "inline" }}
          body="GitHub is cool!"
          imageUrl="https://gitpod.io/images/github.svg"
        />
        <MediaCard
          title="GitLab"
          body="GitLab is cool!"
          imageUrl="https://gitpod.io/images/gitlab.svg"
        />
        <MediaCard
          title="Docker"
          body="Docker is cool!"
          imageUrl="https://www.pikpng.com/pngl/b/430-4307964_docker-and-kubernetes-logos-point-of-sales-icon.png"
        />
        <MediaCard
          title="Gitpod"
          body="Gitpod is cool!"
          imageUrl="https://pbs.twimg.com/profile_images/1114153393306648578/6O8-Z_Rc_400x400.png"
        />
        <MediaCard
          title="Rust"
          body="Rust is cool!"
          imageUrl="https://cdn.freebiesupply.com/logos/large/2x/rust-logo-png-transparent.png"
        />
      </div>
    </div>
  );
}
