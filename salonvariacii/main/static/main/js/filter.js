
  $(".filter-name").click(function() {
    $(".open, .close", this).toggleClass("hidden");
    $(this).find(".sub-menu").slideToggle();
    
    // Закрываем другие открытые выпадающие меню
    $(".filter-name").not(this).find(".sub-menu").slideUp();
    $(".filter-name").not(this).find(".open").addClass("hidden");
    $(".filter-name").not(this).find(".close").removeClass("hidden");
  });

  const resultsDiv = document.getElementById('filtered-results');
  $(".filter-desc li").click(function() {
    console.log(this.innerHTML)
    //если в фильтрации нет элементов
    if ($(".filter .select").length == 1){
      $(".filter .select .clean").remove();
    }
    // если фильтрация еще не проводилась и нет блока "очистить"
    if ($(".filter .select .clean").length == 0){
      const clear = document.createElement('div');
      clear.innerHTML = `
        <div class="clean">Очистить</div>
        `;
      $(".filter .select").append(clear);
    }
    console.log($('.filter-desc li').filter(function() {
      return $(this).text() === this.innerHTML;
    }).length);
    if ($('.filter-desc li').filter(function() {
      return $(this).text() === this.innerHTML;
    }).length == 0) {
      const select = document.createElement('div');
      select.innerHTML = `
        <div class="selected">{this.innerHTML}</div>
        `;
      $(".filter .select").append(select);
      console.log("Блок с указанным innerHTML существует.");
    }
    

  });


//функция фильтрации
document.addEventListener('DOMContentLoaded', function () {
  const resultsDiv = document.getElementById('filtered-results');
  

  form.addEventListener('сlick', async function (event) {
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
