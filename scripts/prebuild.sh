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
echo "Process: $(pidof target/debug/$program_name)"
killall -9 $(pidof target/debug/$program_name)
echo "command `cargo run` successfully cached"
