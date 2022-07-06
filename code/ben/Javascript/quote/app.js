quote = axios.get('https://favqs.com/api/qotd')
.then(function (response) {
  console.log(response.data.quote);
})
.catch(function (error) {
  console.log(error);
})

function getQuote(){
  let result = document.getElementById('generator');
  result.innerHTML = '';

  axios.get('https://favqs.com/api/qotd')
  .then(function (response) {
    result.innerHTML = quoteGenerator(response);
  })
  .catch(function (error){
    result.innerHTML = quoteGeneratorError(error);
  });
}

function quoteGenerator(response) {  
  return  '<h5>ID:</h5>' +
          '<h6>' + JSON.stringify(response.data.quote.id) + '</h6>'+
          '<h5>Author:</h5>' +
          '<h6>' + JSON.stringify(response.data.quote.author) + '</h6>'+
          '<h5>Quote:</h5>' +
          '<h6>' + JSON.stringify(response.data.quote.body) + '</h6>';
}



