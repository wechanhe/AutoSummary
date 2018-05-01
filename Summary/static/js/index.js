        $(document).ready(function(){
            $(".table tr td center a").click(function(){
                <!--生成文摘-->
                var option = $(this).text()
                var name = $(this).attr("name");
                if(option === "生成文摘"){
                    $.ajax({
                      type: 'POST',
                      url: '/summary/generate/',
                      data: {"name":name},
                      success:function(){
                      }
                    });
                }
                <!--删除文件-->
                else if(option === "删除"){
                    $.ajax({
                      type: 'POST',
                      url: '/summary/delete/',
                      data: {"name":name},
                      success:function(result){
                        if(result == "success"){
                            alert("文件已经删除");
                            window.location.href="/summary/index";
                        }else if(result == "fail"){
                            alert("内部错误")
                        }
                      }
                    });
                }

                else if(option === "下载"){
                    $.ajax({
                      type: 'POST',
                      url: '/summary/download/',
                      data: {"name":name},
                      success:function(result){
                        if(result == "success"){
                            alert("文件下载成功");
                            window.location.href="/summary/index";
                        }else if(result == "fail"){
                            alert("内部错误")
                        }
                      }
                    });
                }
            });
        });