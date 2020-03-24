use rusqlite::{params, Connection};
use std::fmt::{self, Display, Formatter};

struct Person {
    id: i32,
    name: String,
    age: i32,
}

impl Display for Person {
    fn fmt(&self, f: &mut Formatter<'_>) -> fmt::Result {
        write!(
            f,
            "{} is {} years old and their #ID is {}",
            self.name, self.age, self.id
        )
    }
}

fn main() -> rusqlite::Result<()> {
    let connection = Connection::open("sql/test.db")?;
    let mut stmt = connection.prepare("SELECT * FROM USER")?;
    let person_iter = stmt.query_map(params![], |row| {
        Ok(Person {
            id: row.get(0)?,
            name: row.get(1)?,
            age: row.get(2)?,
        })
    })?;
    for i in person_iter {
        println!("{}", i?);
    }
    Ok(())
}
