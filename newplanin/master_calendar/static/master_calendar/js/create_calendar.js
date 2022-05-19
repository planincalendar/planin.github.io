let calendar = null;

window.onload = onLoadActions;

function onLoadActions (){
    drawCalendar();
}

//캘린더 옵션
function drawCalendar() {
    let calendarEl = document.getElementById('calendar');
    console.log(document.getElementById("calendar-start-date").value);
    console.log(document.getElementById("calendar-end-date").value);
    
    calendar = new FullCalendar.Calendar(calendarEl, {
        
        scrollTime: '08:00:00',
        businessHours : false,
        expandRows: true,
        longPressDelay: 1000,
        slotMinTime: '06:00',
        slotMaxTime: '20:00',
        dragScroll: true,
        editable: true,
        droppable: true,
        themeSystem: 'bootstrap5',
        windowResizeDelay : 0,
        // timeZone: 'GMT+9',
        initialView: 'timeGridWeek',
        validRange: { 
            // start : start_date
            start : new Date(document.getElementById("calendar-start-date").value),
            end : new Date(document.getElementById("calendar-end-date").value),
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
            let title = '가능한 시간'
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
calendar.addOption('themeSystem', 'bootstrap')

// 일정 조정 기간 세팅하기 ... End date 가 자꾸 하루 전에 생성됨..
function setBackgroundTime(start_date,end_date){
    const cal_start_date = document.getElementById("calendar-start-date");
    const cal_end_date = document.getElementById("calendar-end-date");
        var payload = {
        start : cal_start_date.value,
        end : cal_end_date.value
        }
    calendar.setOption('validRange', payload);
}


async function getCalendarInfo (){
    let response = await fetch('/calendar/<str:pid>/<str:pass_key>/',{
        method: "GET",
        body: JSON.stringify(),
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



//일정 제출하기
async function sendAllEvents(pass_key,pid){
    console.log(pass_key,pid)
    let allEvents = calendar.getEvents();
    
    let payload = {
        slots: [],
    };

    allEvents.forEach(eventData => {
        payload.slots.push({
            "name" : eventData.title,
            "start_timedate": eventData.start,
            "end_timedate" : eventData.end,
            "pass_key": pass_key,
            "pid": pid
        })
    });
    
    //받은 데이터 묶음 장고 모델로 보내기//수정하기 버튼 막기
    let button  = document.getElementById("data-load");
    button.disabled = true

    let result = await eventsToModel(payload,pid,pass_key);
    if (!result){
        alert("일정 제출에 실패했습니다.");
        return;
    }
    alert('일정 제출이 완료되었습니다.');
    location.href = "https://hiplanin.shop/calendar/thankyou/";
    
}

async function eventsToModel(payload,pid,pass_key){
    let response = await fetch(`/calendar/${pid}/${pass_key}/save-events/`,{
        method: "POST",
        body: JSON.stringify(payload),
        headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": getCsrfToken(),
        }
    })

    if (response.status != 200){
        console.log('모델에 이벤트를 보낼 수 없습니다.')
        return false;

    }
    return true;
}

function getCsrfToken() {
    return document.cookie.split("&")
        .find(item => item.includes("csrftoken"))
        .split("=")[1];
}

// function showCommonEvent(user_id){
//     let checkbox = document.getElementById("common-event-checkbox")
//     if (checkbox.checked){
//         addEventList(user_id)
//     }else{
//         removeEventList(user_id)
//     }
// }

//내 일정을 캘린더에 보여주고 지우기

function showEventof(user_id,pid,pass_key){
let checkbox = document.getElementById("my-event-checkbox")
    if (checkbox.checked){
        addEventList(user_id,pid,pass_key)
    }else{
        removeEventList(user_id,pid,pass_key)
    }
}
function addEventList(user_id,pid,pass_key){
    loadEventList(user_id,pid,pass_key).then(eventList => {
        for (const e of eventList.events) {
            let eventData = {
                start: e.start_timedate,
                end: e.end_timedate,
                title: e.name,
                id: e.creator_id,
            }
            calendar.addEvent(eventData);
        }
    })    
}
function removeEventList(user_id,pid,pass_key){
    loadEventList(user_id,pid,pass_key).then(eventList => {
        for (const e of eventList.events) {
            let event_id = e.creator_id 
            let event_of_the_id = calendar.getEventById(event_id)
            event_of_the_id.remove()
            }
    })
}
async function loadEventList(user_id,pid,pass_key){
    let payload = {
        creator_id: user_id
    }
    let response = await fetch(`/calendar/${pid}/${pass_key}/load-events/`,{
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
    
   
