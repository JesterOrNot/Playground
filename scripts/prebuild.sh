IFS=" = "
str=$(awk -F: '/^name/' Cargo.toml)
read -ra ADDR <<< "$str"
program_name="${ADDR[1]}"
program_name=${program_name//'"'/""}
nohup cargo run &
gp await-port 8000
kill $(pidof target/debug/$program_name)
