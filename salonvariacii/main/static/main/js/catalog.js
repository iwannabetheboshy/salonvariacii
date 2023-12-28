$(document).ready(function () {
  var header = document.querySelector("header");
  header.classList.add("catalogCard");
});

function sleep(milliseconds) {
  const date = Date.now();
  let currentDate = null;
  do {
    currentDate = Date.now();
  } while (currentDate - date < milliseconds);
}

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

    if (value !== 'Любой материал' && value !== 'Очистить' && value !== 'Любой метод открытия' && value !== 'Любой стиль') {
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

  var searcInput = $('input[name=search]').val();
  if(searcInput === " "){
    searcInput = "  ";
  }
  
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

    if (searcInput){
      
      if(!($(this).attr('data-name').toLowerCase().includes(searcInput.toLowerCase()
      ))){
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
    $("#catalog-filter .select").css("max-height", "0");
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

function addSelect(parentId, selectName){
  var size = $("#catalog-filter").attr('data-size');
  var select = $(`
    <div class="selected" id="${parentId}"  style="font-size: ${size}px"> 
    ${selectName}
    <svg  width="16" height="16" viewBox="0 0 16 16" fill="none" xmlns="http://www.w3.org/2000/svg">
      <path d="M8.00047 7.05767L11.3003 3.75781L12.2431 4.70062L8.94327 8.00047L12.2431 11.3003L11.3003 12.2431L8.00047 8.94327L4.70062 12.2431L3.75781 11.3003L7.05767 8.00047L3.75781 4.70062L4.70062 3.75781L8.00047 7.05767Z" fill="#1E1E1E"/>
    </svg>
    `);
    $("#catalog-filter .select").append(select);
}

//создание плиток фильтрации для desc
$(".filter-desc li").click(function () {
  const clickedContent = this.innerHTML;
  // если фильтрация еще не проводилась и нет блока "очистить"
  addClean()
  const parentId = $(this).closest('.filter-name').attr('id');

  //добавляем блок в выбранные фильтры, если его там нет
  if ($('#catalog-filter .select .selected').filter(function () {
    return $(this).text().trim() === clickedContent;
  }).length == 0 ) {

    //если уже есть какой нибудь фильтр с parentId, то удаляем (единственный выбор)
    if ($('#catalog-filter .select .selected').filter(function () {
      return $(this).attr('id') === parentId;
    }).length != 0){
      $('#catalog-filter .select').find(`#${parentId}`).remove()
    }


    if (this.innerHTML == 'Любой'){
      if(parentId == 'material'){
        selectName = this.innerHTML + ' материал';
      }else if (parentId == 'openingMethod'){
        selectName = this.innerHTML + ' метод открытия';
      }else{
        selectName = this.innerHTML + ' стиль';
      }
    }else{
      selectName = this.innerHTML;
      
    }
    
    addSelect(parentId, selectName)
    filtration();
  }


});

function addClean(){
  var size = $("#catalog-filter").attr('data-size');
  if ($("#catalog-filter .select .clean").length == 0) {
    var div = $(`<div class="selected clean" id="clean" style="font-size: ${size}px">Очистить</div>`);
    var svg = $('<svg width="16" height="16" viewBox="0 0 16 16" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M8.00047 7.05767L11.3003 3.75781L12.2431 4.70062L8.94327 8.00047L12.2431 11.3003L11.3003 12.2431L8.00047 8.94327L4.70062 12.2431L3.75781 11.3003L7.05767 8.00047L3.75781 4.70062L4.70062 3.75781L8.00047 7.05767Z" fill="#1E1E1E"/></svg>');

    div.append(svg);
    

    $("#catalog-filter .select").prepend(div);
    $("#catalog-filter .select").css("max-height", ($("#catalog-filter .select")[0].scrollHeight) + "px");
  }
}

//поиск
$("#catalog-filter .search-div svg").click(function () {
  addClean()
  filtration();
});

//поиск по enter
$(".filter-seacrh").on("keyup", function (event) {
  if (event.key === "Enter") {
    addClean()
    filtration();
  }
});

//создание плиток фильтрации для mobile
$("#catalog-filter .modal-dialog .filter-save").click(function () {
  var selectedRadioValue = $(".modal-body input[type='radio']:checked");

  $(".select").empty();

  addClean();

  //добавляем блок в выбранные фильтры 
  if (selectedRadioValue.length !== 0) {
    selectedRadioValue.each( function(){
      var parentId = $(this).attr('id');
      if ($('#catalog-filter .select .selected').filter(function () {
        return $(this).attr('id') === parentId;
      }).length != 0){
        $('#catalog-filter .select').find(`#${parentId}`).remove()
      }
      if ($(this).val() == 'Любой'){
        if(parentId == 'material'){
          selectName = $(this).val() + ' материал';
        }else if (parentId == 'openingMethod'){
          selectName = $(this).val() + ' метод открытия';
        }else{
          selectName = $(this).val() + ' стиль';
        }
  
      }else{
        selectName = $(this).val();
      }
  
      addSelect(parentId, selectName)
      $("#catalog-filter .select").css("max-height", ($("#catalog-filter .select")[0].scrollHeight) + "px");
      filtration();
    });
  }
  
});


//отчистка radio из модального окна mobile
$("#catalog-filter .modal-header .modal-clean").click(function () {
  cleanCheck();
  $(".select").empty();
})

function cleanCheck() {
  $('.search-div input[name=search]').val('');
  var selectedRadioValue = $(".modal-body input[type='radio']:checked");
  selectedRadioValue.each(function() {
    $(this).prop('checked', false);
  });
}

$(document).ready(function () {
  $(".catalog-video-container").on("mouseenter", function () {
    yt_container = this.querySelector(".youtube-container")
    var url = yt_container.getAttribute("data-url");
    if(url != "None"){
      if (yt_container.getAttribute("data-load") == 0) {
        var url = yt_container.getAttribute("data-url");
        yt_container.innerHTML = `<iframe src="https://www.youtube.com/embed/${url}?autoplay=1&mute=1&loop=1&color=white&controls=0&modestbranding=1&playsinline=1&rel=0&enablejsapi=1" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>`;
        yt_container.setAttribute("data-load", "1");
        
        setTimeout(function() {
          var iframe = yt_container.getElementsByTagName("iframe")[0].contentWindow;
          iframe.postMessage('{"event":"command","func":"playVideo","args":""}', "*");
        }, 300); 
        $(this).find("img").addClass("hide-image");
        
    }
    else {
        $(this).find("img").addClass("hide-image");
        var iframe = yt_container.getElementsByTagName("iframe")[0].contentWindow;
        iframe.postMessage('{"event":"command","func":"playVideo","args":""}', "*");
    }
    }
  });

  $(".catalog-video-container").on("mouseleave", function () {
    $(this).find("img").removeClass("hide-image");
    yt_container = this.querySelector(".youtube-container")
    var url = yt_container.getAttribute("data-url");
    if(url != "None"){
        try{
          var iframe = yt_container.getElementsByTagName("iframe")[0].contentWindow;
          if(iframe.constructor.name === 'Window'){
            setTimeout(function() {
              iframe.postMessage('{"event":"command","func":"pauseVideo","args":""}', "*");
            }, 1500);
          }
        }
        catch{
          iframe.postMessage('{"event":"command","func":"pauseVideo","args":""}', "*");
        }
      }
        
       
  });
});
