function validation() {  
    var id = document.f1.user.value;  
    var ps = document.f1.pass.value;
    var sc = document.f1.spec.value; 
    if(id.length === 0 || ps.length === 0 || sc.length === 0) {  
        alert("All fields are required");  
        return false;  
    }  
}
