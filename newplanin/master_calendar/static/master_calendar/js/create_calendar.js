let calendar = null;
window.onload = onLoadActions;

function onLoadActions (){
    drawCalendar();
}

//캘린더 옵션
function drawCalendar() {
    let calendarEl = document.getElementById('calendar');
    
    calendar = new FullCalendar.Calendar(calendarEl, {
        scrollTime: '08:00:00',
        businessHours : false,
        expandRows: true,
        longPressDelay: 1000,
        slotMinTime: '00:00',
        slotMaxTime: '24:00',
        dragScroll: true,
        editable: true,
        droppable: true,
        themeSystem: 'bootstrap5',
        timeZone: 'GMT+9',
        initialView: 'timeGridWeek',
        validRange: {
          },
//        firstDay: (new Date().getDay()), 
        headerToolbar: {
            left: 'prev,next',
            center: 'title',
            right: 'today',
        },
        events : [
            
        ],
        // 신규 이벤트 생성 
        selectable: true,
        selectConstraint: null, 
        selectMirror: true,
        select: function(arg) {
            let title = prompt('일정 내용:');
            if (title) {
            calendar.addEvent({
                title: title,
                start: arg.start,
                end: arg.end,
                allDay: arg.allDay
            })
            }
            calendar.unselect()
        },
        eventClick: function(arg) {
            if (confirm('이벤트를 삭제하시겠습니까?')) {
            arg.event.remove()
            }
        },
        editable: true,
       
    });

    calendar.render();
}    
//일정 조정 기간 세팅하기 ... End date 가 자꾸 하루 전에 생성됨..
function setBackgroundTime(){
    const cal_start_date = document.getElementById("calendar-start-date");
    const cal_end_date = document.getElementById("calendar-end-date");
    //두 필드가 입력되면 캘린더 옵션에 validRange집어 넣기
    if (!cal_start_date.value){
        alert('시작 기간을 입력해주세요!')
    }else if (!cal_end_date.value) {
        alert('끝 기간을 입력해주세요!')
    }else{
        var payload = {
        start : cal_start_date.value,
        end : cal_end_date.value
    }
    calendar.setOption('validRange', payload);
    }
}



//일정 제출하기
async function sendAllEvents(user_id){
    console.log(user_id)
    let allEvents = calendar.getEvents();
    
    let payload = {
        slots: [],
    };
    
    allEvents.forEach(eventData => {
        payload.slots.push({
            "name" : eventData.title,
            "start_timedate": eventData.start,
            "end_timedate" : eventData.end,
            "creator_id": user_id,
        })
    });

    //받은 데이터 묶음 장고 모델로 보내기
    let result = await eventsToModel(payload);
    
    if (!result){
        alert("일정 제출에 실패했습니다.");
        return;
    }
    alert('일정 제출이 완료되었습니다.');
    let button  = document.getElementById("data-load");
    button.disabled = true

    
    //제출하기 버튼이 수정하기로 변하기 
    // const element = document.getElementById("data-upload");
    // element.innerHTML = "수정하기";

}

async function eventsToModel(payload){
    let response = await fetch('/calendar/save-events/',{
        method: "POST",
        body: JSON.stringify(payload),
        headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": getCsrfToken(),
        }
    });
    if (response.status != 200){
        return false;
    }
    return true;
}

function getCsrfToken() {
    return document.cookie.split("&")
        .find(item => item.includes("csrftoken"))
        .split("=")[1];
}

//내 일정을 캘린더에 보여주고 지우기
function showCommonEvent(user_id){
    let checkbox = document.getElementById("common-event-checkbox")
    if (checkbox.checked){
        addEventList(user_id)
    }else{
        removeEventList(user_id)
    }
}


function showEventof(user_id){
let checkbox = document.getElementById("my-event-checkbox")
    if (checkbox.checked){
        addEventList(user_id)
    }else{
        removeEventList(user_id)
    }
}
function addEventList(user_id){
    loadEventList(user_id).then(eventList => {
        for (const e of eventList.events) {
            let eventData = {
                start: e.start_date,
                end: e.end_date,
                title: e.title,
                id: e.owner_id,
            }
            calendar.addEvent(eventData);
        }
    })    
}
function removeEventList(user_id){
    loadEventList(user_id).then(eventList => {
        for (const e of eventList.events) {
            let event_id = e.owner_id 
            let event_of_the_id = calendar.getEventById(event_id)
            event_of_the_id.remove()
            }
    })
}
async function loadEventList(user_id){
    let payload = {
        owner_id: user_id
    }
    let response = await fetch('/calendar/load-events/',{
        method: "POST",
        body: JSON.stringify(payload),
        headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": getCsrfToken(),
        }
    });
    if (response.status == 200){
        let responseBody = await response.json();
        return responseBody;        
    }else {
        alert('이벤트를 불러오는데 실패했습니다.')
    }
}



// allEvents.forEach(eventData => {
//     console.log(eventData.title);
//     console.log(eventData.start);
//     console.log(eventData.end);
//     payload.events.push({
//         "title" : eventData.title,
//         "start": eventData.start,
//         "end" : eventData.end,
//     })
// 
    // for eventEl of eventlist 
    //     start: eventEl.start_date,
    //     end: eventEl.end_date,
    //     calendar.addEvent({
    
   
