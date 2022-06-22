function sortByPriceAscending(jsonString) {
  const jsonData = JSON.parse(jsonString);
  jsonData.sort((a, b) => a.price - b.price);
  jsonData.sort((a, b) => a.price === b.price && String(a.name).localeCompare(String(b.name)));
  return JSON.stringify(jsonData);
}

console.log(
  sortByPriceAscending(
    '[{"name":"eggs","price":1},{"name":"coffee","price":9.99},{"name":"rice","price":4.04}]'
  )
);
