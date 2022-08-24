const formEl = document.querySelector("form");
    const tbodyEl = document.querySelector('tbody');
    function onAddUser(e) {
    //e.preventDefault();
    const u = document.getElementById("select");
    const displaytext = u.options[u.selectedIndex].text;
    const selectUser = document.getElementById("select").value=displaytext;
    const tableEl = document.querySelector('table');
    tbodyEl.innerHTML += `
        <tr>
            <td>${selectUser}</td>
            <td><button type="button" class="btn btn-outline-secondary" onclick="removeUser(this)"><i class="fa fa-trash" aria-hidden="true"></i></button></td>
        </tr>
    `;
    alert(selectUser);
    }
    formEl.addEventListener("droit d'accès", onAddUser);

    function removeUser(r){
        var i = r.parentNode.parentNode.rowIndex;
        document.getElementById("tb1").deleteRow(i);
    }

        document.getElementById("btn1").addEventListener("click",function() {
        var box1 = document.getElementById("tb1");
            if(box1.style.display=="none")
            {
                box1.style.display="table";
                box1.style.width="100%";
            }
            else
            {
                box1.style.display="none";
            }
        });
