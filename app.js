const http = require('http');
const fs = require('fs')
const port = 3000;
const url = 'https://localhost:5000/topTen'

const server = http.createServer((req, res) => {
    res.writeHead(200, { 'content-type': 'text/html' })
    fs.createReadStream('hackathon.html').pipe(res)
});

server.listen(port, () => {
  console.log(`Server running at port ${port}`);
});