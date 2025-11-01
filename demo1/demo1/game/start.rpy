define role1 = Character('哈基蜂', color="#c8c8ff", image="role1")
define role2 = Character('杀心重的露娜', color="#c8c8ff", image="role2")
define role3 = Character('威风的龙', color="#c8c8ff", image="role3")
define role4 = Character('aaabv', color="#c8c8ff", image="role4")
define role5 = Character('阿虚', color="#c8c8ff", image="role5")
define role6 = Character('春日', color="#c8c8ff", image="role6")
define role7 = Character('春日bbbb', color="#c8c8ff", image="role7")
define narrator_nvl = Character(None, kind=nvl)
define narrator_adv = Character(None, kind=adv)
define config.voice_filename_format = "audio/{filename}"
image side role1 = "images/haruhi 1.png"

label start:
with dissolve
narrator_nvl "交战，搜索，搞定就撤！"
role1 "又是来普坝跑刀的一天^v^"
role1 "看看今天的大免保中会出什么好货呢？"
role2 "我的箭下没有秘密！"
narrator_nvl "位置暴露"
role1 "不要啊让我把东西塞到安全箱。。。额啊啊啊啊啊啊"
with dissolve
narrator_nvl "撤离失败"
role1 "普坝用什么四套三蛋啊，神人来的，经典露娜杀心重，给你得了呗。"
role3 "哈基蜂不要在普坝跑刀了，跟我来绝密航天猛攻！"
role1 "啊，可是我普通模式KD才0.2，我不会拖累你们吗？"
role3 "（已经很久没有出过大红了，急切需要唐人爆率来出点货）当然不会！你只要做好后勤保障就好，猛攻交给我们！"
role1 "好，好吧，那我给你们多带一点药"
narrator_nvl "哈基蜂，威风的龙，善战的狼复活在了二号员工通道"
role3 "我不喜欢这个位置，还好有哈基蜂，我们可以封长烟过点"
menu:
    "跳转到Sheet2":
        jump Sheet2

    "跳转到Sheet3":
        jump Sheet3
