#![feature(proc_macro_hygiene)]
#![feature(decl_macro)]

#[macro_use]
extern crate rocket;

#[get("/")]
fn index() -> String {
    "Hello World From Rocket.rs".to_owned()
}

fn main() {
    rocket::ignite().mount("/", routes![index]).launch();
}

