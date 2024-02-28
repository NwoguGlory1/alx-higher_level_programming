$.ajax({
  url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
  method: 'GET',
  dataType: 'json',
  success: function (data) {
    const movieListHtml = data.results.map(movie => '<li>' + movie.title + '</li>').join('');
    $('UL#list_movies').html(movieListHtml);
  }
});
