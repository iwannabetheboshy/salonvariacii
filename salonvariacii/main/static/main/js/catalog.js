$(document).on("click", function (e) {
  // Проверяем, был ли клик внутри .filter-name или .sub-menu
  if (!$(e.target).closest(".filter-name, .sub-menu").length) {
    // Закрываем все открытые dropdown
    $(".sub-menu").slideUp();
    $(".open").addClass("hidden");
    $(".close").removeClass("hidden");
  }
});

$(".filter-name").click(function () {
  $(".open, .close", this).toggleClass("hidden");

  if ($(window).width() < 1200) {
    $(this).parent().find(".sub-menu").slideToggle();
    $(".filter-name").parent().not($(this).parent()).find(".sub-menu").slideUp();
    $(".filter-name").parent().not($(this).parent()).find(".open").addClass("hidden");
    $(".filter-name").parent().not($(this).parent()).find(".close").removeClass("hidden");
  } else {
    $(this).find(".sub-menu").slideToggle();
    $(".filter-name").not(this).find(".sub-menu").slideUp();
    $(".filter-name").not(this).find(".open").addClass("hidden");
    $(".filter-name").not(this).find(".close").removeClass("hidden");
  }
});

const resultsDiv = $('#filtered-results');
const rezKitchen = $(".result")

async function filtration() {
  $(".none-result").addClass("hidden");
  $(".filtered-results-wrapper").removeClass("hidden");
  const selectedValues = {};
  $('.selected').each(function () {
    const id = $(this).attr('id');
    const value = $(this).text().trim();

    if (value !== 'Любой' && value !== 'Очистить') {
      if (!selectedValues[id]) {
        selectedValues[id] = value;
      } else {
        if (Array.isArray(selectedValues[id])) {
          selectedValues[id].push(value);
        } else {
          selectedValues[id] = [selectedValues[id], value];
        }
      }
    }
  });

  var filtered = rezKitchen;
  var count = 0;
  rezKitchen.each(function () {
    var show = true;

    for (var key in selectedValues) {
      var data = $(this).attr('data-' + key).split(',');

      let intersection = data.filter(x => selectedValues[key].includes(x));
      if (intersection.length === 0) {
        show = false;
      }
    }

    if (show) {
      $(this).show();
      count = count + 1;
    } else {
      $(this).hide();
    }


  });

  if(count === 0){
    $(".none-result").removeClass("hidden");
    $(".filtered-results-wrapper").addClass("hidden");
  }



  $("#catalog-filter .select .selected").click(function () {
    if ($(this).attr('id') === "clean") {
      $(".select").empty();
      cleanCheck();
    } else {
      $(this).remove();
      if ($("#catalog-filter .select div").length === 1) {
        $("#catalog-filter .select .clean").remove();
        cleanCheck();
      }
    }
    filtration();
  });

  $(".catalog-video-container").on("mouseenter", function () {
    $(this).find("img").hide();
    $(this).find("video").trigger('play');

  });

  $(".catalog-video-container").on("mouseleave", function () {
    $(this).find("video").trigger('pause');
    $(this).find("img").show();
  });

}


//создание плиток фильтрации для desc
$(".filter-desc li").click(function () {
  const clickedContent = this.innerHTML;

  // если фильтрация еще не проводилась и нет блока "очистить"
  if ($("#catalog-filter .select .clean").length == 0) {
    var div = $('<div class="selected clean" id="clean">Очистить</div>');
    var svg = $('<svg width="16" height="16" viewBox="0 0 16 16" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M8.00047 7.05767L11.3003 3.75781L12.2431 4.70062L8.94327 8.00047L12.2431 11.3003L11.3003 12.2431L8.00047 8.94327L4.70062 12.2431L3.75781 11.3003L7.05767 8.00047L3.75781 4.70062L4.70062 3.75781L8.00047 7.05767Z" fill="#1E1E1E"/></svg>');

    div.append(svg);
    $("#catalog-filter .select").prepend(div);
  }


  //добавляем блок в выбранные фильтры, если его там нет
  if ($('#catalog-filter .select .selected').filter(function () {
    return $(this).text().trim() === clickedContent;
  }).length == 0) {

    const parentId = $(this).closest('.filter-name').attr('id');


    //проверяем выбран ли уже стиль
    if ($('#catalog-filter .select .selected').filter(function () {
      return $(this).attr('id') === parentId;
    }).length > 0 && parentId === 'style') {
      $('#catalog-filter .select').find(`#${parentId}`).remove()
    }

    var select = $(`
        <div class="selected" id="${parentId}"> 
        ${this.innerHTML}
        <svg  width="16" height="16" viewBox="0 0 16 16" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path d="M8.00047 7.05767L11.3003 3.75781L12.2431 4.70062L8.94327 8.00047L12.2431 11.3003L11.3003 12.2431L8.00047 8.94327L4.70062 12.2431L3.75781 11.3003L7.05767 8.00047L3.75781 4.70062L4.70062 3.75781L8.00047 7.05767Z" fill="#1E1E1E"/>
        </svg>
        `);
    $("#catalog-filter .select").append(select);

    filtration();
  }


});

//поиск
$("#catalog-filter .search-div svg").click(function () {
  filtration();
});

//поиск по enter
$(".filter-seacrh").on("keyup", function (event) {
  if (event.key === "Enter") {
    filtration();
  }
});

//создание плиток фильтрации для mobile
$("#catalog-filter .modal-dialog .filter-save").click(function () {
  var checkedCheckboxes = $(".modal-body input[type='checkbox']:checked");
  var selectedRadioValue = $(".modal-body input[type='radio']:checked");

  $(".select").empty();

  if ($("#catalog-filter .select .clean").length == 0) {

    var div = $('<div class="selected clean" id="clean">Очистить</div>');
    var svg = $('<svg width="16" height="16" viewBox="0 0 16 16" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M8.00047 7.05767L11.3003 3.75781L12.2431 4.70062L8.94327 8.00047L12.2431 11.3003L11.3003 12.2431L8.00047 8.94327L4.70062 12.2431L3.75781 11.3003L7.05767 8.00047L3.75781 4.70062L4.70062 3.75781L8.00047 7.05767Z" fill="#1E1E1E"/></svg>');

    div.append(svg);
    $("#catalog-filter .select").prepend(div);
  }

  if (checkedCheckboxes.length !== 0) {
    //добавляем блок в выбранные фильтры
    checkedCheckboxes.each(function () {
      var select = $(`
        <div class="selected" id="${this.id}"> 
        ${this.value}
        <svg  width="16" height="16" viewBox="0 0 16 16" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path d="M8.00047 7.05767L11.3003 3.75781L12.2431 4.70062L8.94327 8.00047L12.2431 11.3003L11.3003 12.2431L8.00047 8.94327L4.70062 12.2431L3.75781 11.3003L7.05767 8.00047L3.75781 4.70062L4.70062 3.75781L8.00047 7.05767Z" fill="#1E1E1E"/>
        </svg>
        `);
      $("#catalog-filter .select").append(select);
    });
  }
  //добавляем блок в выбранные фильтры стилей
  if (selectedRadioValue.length !== 0) {
    //если стиль уже выбран
    if ($("#catalog-filter .select #style" !== 0)) {
      $('#catalog-filter .select').find(`#style`).remove()
    }

    var select = $(`
        <div class="selected" id="${selectedRadioValue.attr('id')}"> 
        ${selectedRadioValue.val()}
        <svg  width="16" height="16" viewBox="0 0 16 16" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path d="M8.00047 7.05767L11.3003 3.75781L12.2431 4.70062L8.94327 8.00047L12.2431 11.3003L11.3003 12.2431L8.00047 8.94327L4.70062 12.2431L3.75781 11.3003L7.05767 8.00047L3.75781 4.70062L4.70062 3.75781L8.00047 7.05767Z" fill="#1E1E1E"/>
        </svg>
        `);
    $("#catalog-filter .select").append(select);

  }

  filtration();

});


//отчистка checkbox и radio из модального окна mobile
$("#catalog-filter .modal-header .modal-clean").click(function () {

  cleanCheck();

  $(".select").empty();
})

function cleanCheck() {
  $('.search-div input[name=search]').val('');
  var checkedCheckboxes = $(".modal-body input[type='checkbox']:checked");
  var selectedRadioValue = $(".modal-body input[type='radio']:checked");

  checkedCheckboxes.each(function () {
    $(this).prop('checked', false);
  });

  selectedRadioValue.prop('checked', false);
}

$(document).ready(function () {
  $(".catalog-video-container").on("mouseenter", function () {
    $(this).find("img").hide();
    $(this).find("video").trigger('play');

  });

  $(".catalog-video-container").on("mouseleave", function () {
    $(this).find("video").trigger('pause');
    $(this).find("img").show();
  });
});