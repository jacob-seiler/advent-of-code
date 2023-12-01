// Read file
const filename = 'q1.txt';
const data = await Deno.readTextFile(filename)
    .then((data) => data.split('\r\n'));

console.log(data);
