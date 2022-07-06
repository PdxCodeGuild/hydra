function getQuote(){
    let keyWord= prompt("Enter keyword");
    let url = new URL('https://favqs.com/api/quotes?page=1&filter=mark');
    let parameters = url.searchParams;
    parameters.set('filter', keyWord);
    url.search = parameters.toString();
    let new_url = url.toString();
    let result = document.getElementById('generator');
    result.innerHTML = '';
  
    axios.get(new_url, {
        headers: {
            'Authorization': `Token token="1de5edd672daca806221aa868f44a5bc"`
            }
        })

    .then(function (response) {
      result.innerHTML = quoteGenerator(response);
      console.log(response);
    })
    .catch(function (error){
      result.innerHTML = quoteGeneratorError(error);
      console.log(error);
    });
}

function quoteGenerator(response) {
    return  '<h5>ID:</h5>' +
            '<h6>' + JSON.stringify(response.data.quotes[0].id) + '</h6>'+
            '<h5>Author:</h5>' +
            '<h6>' + JSON.stringify(response.data.quotes[0].author) + '</h6>'+
            '<h5>Quote:</h5>' +
            '<h6>' + JSON.stringify(response.data.quotes[0].body) + '</h6>'+

            '<h5>ID:</h5>' +
            '<h6>' + JSON.stringify(response.data.quotes[1].id) + '</h6>'+
            '<h5>Author:</h5>' +
            '<h6>' + JSON.stringify(response.data.quotes[1].author) + '</h6>'+
            '<h5>Quote:</h5>' +
            '<h6>' + JSON.stringify(response.data.quotes[1].body) + '</h6>'+

            '<h5>ID:</h5>' +
            '<h6>' + JSON.stringify(response.data.quotes[2].id) + '</h6>'+
            '<h5>Author:</h5>' +
            '<h6>' + JSON.stringify(response.data.quotes[2].author) + '</h6>'+
            '<h5>Quote:</h5>' +
            '<h6>' + JSON.stringify(response.data.quotes[2].body) + '</h6>';
  }