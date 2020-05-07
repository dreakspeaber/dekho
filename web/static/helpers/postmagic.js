    document.addEventListener('DOMContentLoaded', function() {
    const cols = document.querySelectorAll('.postmagic');
    [].forEach.call(cols, (e)=>{
    e.onclick = function(){
      if(confirm('click ok to confirm the action')){
        const request = new XMLHttpRequest();
        let path = '/' + this.dataset.id + this.dataset.link
        var csrftoken = Cookies.get('csrftoken');
        request.open('POST',path)
        request.setRequestHeader("X-CSRFToken",csrftoken)
        request.onload = () => {
            const data = JSON.parse(request.responseText);
            console.log(data);
            if(data.result===true){
              if(confirm(this.dataset.success)){
                window.location.reload();  
              }
            };
            if(data.result===false){
                alert(this.dataset.failure)
            };

        
        };
        request.send();  
      };
    };
    });

    });