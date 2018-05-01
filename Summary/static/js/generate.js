$(document).ready(function(){
    $("#summarize").click(function(){
        var num = $("#num").val();
        var text = $("#raw_text").val();
        var filename = $("#raw_text").attr("name");
        $.ajax({
            type: 'POST',
            url: '/summary/summarize/',
            data: {"num":num,"text":text,"filename":filename},
            success:function(result){
                alert("文摘生成成功");
                console.log(result);
                $("#result").empty();
                $("#result").html(result);//后台返回直接加进去就行了
            },
            error:function(result){
                console.log(result);
                alert("error");
            }
        });
    });

    $("#raw_text").onchange= function(){
        alert("change");
    };
});