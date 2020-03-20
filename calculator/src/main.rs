#![feature(proc_macro_hygiene, decl_macro)]
#[macro_use]
extern crate rocket;
use rocket::response::NamedFile;
use std::io;

#[get("/")]
fn index() -> io::Result<NamedFile> {
    NamedFile::open("site/index.html")
}

#[get("/style.css")]
fn get_style() -> io::Result<NamedFile> {
    NamedFile::open("site/style.css")
}

fn main() {
    rocket::ignite()
        .mount("/", routes![index, get_style])
        .launch();
}
