//функция фильтрации
document.addEventListener('DOMContentLoaded', function () {
  const form = document.getElementById('filter-form');
  const resultsDiv = document.getElementById('filtered-results');

  form.addEventListener('submit', async function (event) {
    event.preventDefault();

    const formData = new FormData(form);
    console.log(formData);
    try {
      const response = await fetch('/filter/', {
        method: 'POST',
        body: formData,
      });

      if (response.ok) {
        const data = await response.json();
        const filteredKitchens = data.filtered_kitchens;
        // Отчищаем предыдущие результаты
        resultsDiv.innerHTML = '';
        console.log(filteredKitchens);
        // Отобразить отфильтрованные результаты в цикле
        filteredKitchens.forEach(function (kit) {
          const kitDiv = document.createElement('div');
          kitDiv.classList.add('col');

          kitDiv.innerHTML = `
          <br>
          ${kit.name} <br>
          ${kit.style__name}<br>
          ${kit.material__name}<br>
          ${kit.openingMethod__name}<br>
          <br>
          `;
          resultsDiv.appendChild(kitDiv);
        });

      } else {
        resultsDiv.innerHTML = 'Ошибка при выполнении запроса';
      }
    } catch (error) {
      resultsDiv.innerHTML = 'Ошибка при выполнении запроса: ' + error;
    }
  });
});
