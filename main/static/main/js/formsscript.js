
const distanceSelect = document.getElementById('id_distance');
const options = distanceSelect.options;

for (let i = 0; i < options.length; i++) {
  if (options[i].value === '0.0') {
    // console.log(options[i].value)
    options[i].text = 'Нет данных';
    break;
  }
}



document.addEventListener('DOMContentLoaded', refreshFilter);
document.getElementById('main-form').addEventListener('change', refreshFilter);

function refreshFilter(){
    const prametersObject = {};
    const selects = document.getElementsByTagName('select')
    for (let i=0; i<selects.length; i++){
        let selectedOptions = Array.from(selects[i].options).filter(option => option.selected).map(option => option.value);
        if (selectedOptions.length > 0) {
            property = selects[i].id.slice(3, )
            prametersObject[property] = selectedOptions
        }
    }
    // console.log(prametersObject)
    let token = getCookie('csrftoken');

    $.ajax({
        headers: {"X-CSRFToken": token},
        url: "/induktivnye-datchiki/ajaxform/",
        type: 'post',
        data: JSON.stringify(prametersObject),
        contentType: 'application/json',
        success: function(response) {
            // console.log(response);
            for (let param=0; param<selects.length; param++){       //цикл по параметрам
                if (param === 'sort_by'){continue;}
                // console.log(selects[param].name)
                let OptionsType = Array.from(selects[param].options);
                for (option in OptionsType){            //цикл по значениям параметров
                    if (response[selects[param].name] === undefined){break}
                    // console.log('ответ ',  response[selects[param].name])
                    // console.log('поиск в ответе ', OptionsType[option].value);
                    // console.log(response[selects[param].name].indexOf(OptionsType[option].value) === -1)
                    OptionsType[option].style.color = 'black'
                    OptionsType[option].style.fontWeight = 450;
                    let fieldValue = OptionsType[option].value;
                    if (selects[param].name === 'distance'){
                        fieldValue = Number(OptionsType[option].value)
                    }
                    if (response[selects[param].name].indexOf(fieldValue) === -1 ){//-1 если индекса нет
                        // console.log('Нет')
                        OptionsType[option].style.color = 'grey'
                        OptionsType[option].style.fontWeight = 400;
                    }
                }
            }
        },
        error: function(xhr, status, error) {
            console.error('Error saving data: ' + error);
          }
    });

            // selectedOptions.style.color = 'grey';
}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();

            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
