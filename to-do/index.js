const express = require('express');
const app = express()

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({extended: true}));
app.use(express.static)

app.get('/', function(req, res){
  res.sendFile('index.html');
});

//app.use('/api/todos', todoRoutes);

app.listen(3000, () => {
  console.log('App listening on port 3000!')
})
