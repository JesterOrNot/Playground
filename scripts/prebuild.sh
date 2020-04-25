echo "Starting..."
IFS=" = "
str=$(awk -F: '/^name/' Cargo.toml)
read -ra ADDR <<< "$str"
program_name="${ADDR[1]}"
program_name=${program_name//'"'/""}
echo "Crate name: $program_name"
nohup cargo run &
gp await-port 8000
echo "Killing process"
kill -9 $(pidof target/debug/$program_name)
