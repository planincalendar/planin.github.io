
function sendAlertNewProject() {
    const project_name = document.getElementById("project-name-input")
    const cal_start_date = document.getElementById("calendar-start-date-input");
    const cal_end_date = document.getElementById("calendar-end-date-input");
    const shared_user_name_email = document.getElementById("project-shared-user-input");
    
    if (!project_name.value){
        alert('프로젝트 이름을 입력해주세요!') 
        return false;
    }else if(!cal_start_date.value){
        alert('조정 시작 기간을 입력해주세요!')
        return false;
    }else if (!cal_end_date.value) {
        alert('조정 끝 기간을 입력해주세요!')
        return false;
    }else if (!shared_user_name_email.value) {
        alert('면접관 이름과 이메일을 한 명 이상 입력해주세요!')
        return false;
        // 면접관 이름과 이메일, 한 명 이상인 지 확인
    } else {
        shared_user = document.getElementById("project-shared-user-input")
        console.log(shared_user.value)
        alert('프로젝트가 생성되었습니다.');
        //데이터를 확인할 수 있는 모달 -> 최종 제출 버튼 
        }
}

function sendAlertEditProject(){
    alert('포지션 정보가 수정되었습니다.')

}

