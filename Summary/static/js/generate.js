$(document).ready(function(){
    $("#summarize").click(function(){
        var num = trim($("#num").val());
        var text = $("#raw_text").val();
        var filename = $("#raw_text").attr("name");
        console.log(isIntNum(num));
//        if(isIntNum(num) == false){
//            alert("请输入数字");
//            return;
//        }else{
//            num = paseInt(num);
//        }
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

function isIntNum(val){
    var regPos = / ^\d+$/; // 非负整数
    var regNeg = /^\-[1-9][0-9]*$/; // 负整数
    if(regPos.test(val) || regNeg.test(val)){
        return true;
    }else{
        return false;
    }
}

function trim(str) {
    return str.replace(/(^\s+)|(\s+$)/g,"");
}