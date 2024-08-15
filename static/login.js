$(document).ready(function() {
    $('#loginForm').on('submit', function(event) {
        event.preventDefault();
        
        var username = $('#username').val();
        
        // 在这里可以将用户名发送到后端进行处理
        
        // 可以在这里执行其他操作，比如重定向到其他页面
        // window.location.href = '/dashboard';
    });
});