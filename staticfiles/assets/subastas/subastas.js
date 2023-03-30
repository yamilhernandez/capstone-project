

  function makeTableScroll() {
    // Constant retrieved from server-side via JSP
    var maxRows = 8;
    var table = document.getElementById('myTable');
    var wrapper = table.parentNode;
    var rowsInTable = table.rows.length;
    var height = 6;
    if (rowsInTable > maxRows) {
      for (var i = 0; i < maxRows; i++) {
        height += table.rows[i].clientHeight;
      }
      wrapper.style.height = height + "px";
    }
  }
      function makeTableScrollEmergencia() {
        // Constant retrieved from server-side via JSP
        var maxRows = 8;
        var table = document.getElementById('myTable');
        var wrapper = table.parentNode;
        var rowsInTable = table.rows.length;
        var height = 6;
        if (rowsInTable > maxRows) {
          for (var i = 0; i < maxRows; i++) {
            height += table.rows[i].clientHeight;
          }
          wrapper.style.height = height + "px";
        }
      }
   
  document.addEventListener("DOMContentLoaded", () => {
    const rows = document.querySelectorAll("tr[data-href]");
    rows.forEach(row => {
      row.addEventListener("click",()=>{
        window.location.href = row.dataset.href;
      });
    });
  });

  document.addEventListener("DOMContentLoaded", () => {
    const rows = document.querySelectorAll("td[data-href]");
    rows.forEach(row => {
      row.addEventListener("click",()=>{
        window.location.href = row.dataset.href;
      });
    });
  });


  /* Nav Bar Gobierno */
                                          
  const openClick = () => {
    if (!openInfo.classList.contains("scrollAnimation")) {
      openInfo.classList.add("scrollAnimation");
      arrow.classList.add("arrow-rotate");
      setTimeout(function () {
        navIcon.classList.add("hidden");
      }, 200);
    } else if (openInfo.classList.contains("scrollAnimation")) {
      openInfo.classList.remove("scrollAnimation");
      arrow.classList.remove("arrow-rotate");
      setTimeout(function () {
        navIcon.classList.remove("hidden");
      }, 500);
    }
  };
  
                            
                          
                          
                        
                      
                    