const express = require('express');
const app = express();
const request = require('request')

app.get('/results', function(req, res){
  request('http://omdbapi.com/?s=california', function(error, response, body){
    if(!error && response.statusCode == 200){
      res.send(body);
    }
  });

})

app.listen(process.env.PORT, process.env.IP, function(){
  console.log('Server is running')
})
