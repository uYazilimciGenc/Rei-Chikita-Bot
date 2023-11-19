import praw
import chikilib
import time

reddit = praw.Reddit(
    client_id="",  # API Client ID Goes Here
    client_secret="",  # Client Secret Code Goes Here
    user_agent="",  # Define an user agent
    username="",  # Username
    password=""  # Password
)

print("****************")


merhabaArr = ["merhaba", "merhabalar", "mrb", "naber", "hello", "hallo", "slm", "selam"]
sagolArr = ["sağol", "sagol", "tesekkur", "tesekkurler", "teşekkür", "teşekkürler", "tşk", "eyw"]
ovguArr = ["good bot", "iyi bot", "nice bot", "based bot"]
gunaydinArr = ["günaydın", "gunaydin", "günaydin", "gunaydın"]
gnightArr = ["iyi geceler", "iyi akşamlar", "iyi aksamlar", "ıyı aksamlar"]
ilyArr = ["seviyorum seni", "seni seviyorum", "i love u", "i love you", "ily", "<3", "sana aşığım", "sana asigim"]
nasilsinArr = ["nasılsın", "nasilsin", "naber", "keyfin nasıl", "keyfin nasil", "hayat nasıl gidiyor", "keyifler nasıl", "iyi misin"]
#-----------------Komutlar----------------
help = ["!help", "!yardim", "!yardım"]
puanKomut = ["!puan", "!cikipuan"]
top = ["!top", "!leaderboard", "!top5"]

time_sleep = 2
def checkKeyword(base, array):
    #found = False
    # for keyword in array:
    #     if keyword in base:
    #         found = True
    #         break
    found = any(keyword in base for keyword in array)
    return found

def checkComment(comment, commands):
    return comment in commands

def replyCheck():
    time.sleep(time_sleep)
    for reply in reddit.inbox.comment_replies():
        if reply.new:
            print("****** Replied ******")
            print(reply.author)
            print(reply.body)

            chikilib.puan_ekle(reply.author, 5)

            replyMessage = reply.body.lower()

            _repMessage = ""

            if checkKeyword(replyMessage, merhabaArr) and reply.author != reddit.user.me():
                print("***** Reply To *****")
                _repMessage = ":) Merhaba " + str(reply.author) + "!"
                reply.reply(_repMessage)

            elif checkKeyword(replyMessage, sagolArr) and reply.author != reddit.user.me():
                print("***** Reply To *****")
                _repMessage = "Bişi diğil \^^"
                reply.reply(_repMessage)
            elif checkKeyword(replyMessage, ovguArr) and reply.author != reddit.user.me():
                print("***** Reply To *****")
                _repMessage = "Teşekkürler! Ben de senin iyi olduğunu düşünüyorum :)"
                reply.reply(_repMessage)
            elif checkKeyword(replyMessage, gunaydinArr) and reply.author != reddit.user.me():
                print("***** Reply To *****")
                _repMessage = "Sana da günaydın <3"
                reply.reply(_repMessage)
            elif checkKeyword(replyMessage, gnightArr) and reply.author != reddit.user.me():
                print("***** Reply To *****")
                _repMessage = "Sana da iyi geceler <3"
                reply.reply(_repMessage)
            elif checkKeyword(replyMessage, ilyArr) and reply.author != reddit.user.me():
                print("***** Reply To *****")
                _repMessage = "Ben de seni seviyorum " + \
                    str(reply.author) + " \^^"
                reply.reply(_repMessage)
            elif checkKeyword(replyMessage, nasilsinArr) and reply.author != reddit.user.me():
                print("***** Reply To *****")
                _repMessage = "İyiyim, umarım sen de iyisindir! \^_^"
                reply.reply(_repMessage)
            #------------------Komutlar------------------
            elif checkComment(replyMessage, puanKomut) and reply.author != reddit.user.me():
                print("***** Reply To {} *****".format(reply.author))
                puan = chikilib.kac_puan(reply.author)
                _repMessage = "Merhaba, {}. Mevcut 🪙Çikipuan durumunuzu aşağıdaki tabloda görüntüleyebilirsiniz!\n\n**Kullanıcı**|**🪙Çikipuan**\n:--|:--:\n{}|🪙{}\n\n^(Ben bir botum ve bu eylem otomatik olarak gerçekleştirildi. Kullanılabilecek diğer komutlar için !help veya !yardim ile yanıtlayın.)".format(reply.author, reply.author, puan)
                reply.reply(_repMessage)
            elif checkComment(replyMessage, top) and reply.author != reddit.user.me():
                print("***** Reply To {} *****".format(reply.author))
                _repMessage = "Selamlar \^\^. İşte en çok Çikipuan'a sahip o kutsal kişiler!\n\n**No**|**Kullanıcı**|**🪙Çikipuan**\n--:|:--|:--:"
                top5 = chikilib.top_5()
                for idx, user in enumerate(top5):
                    _repMessage += "\n{}|{}|🪙{}".format(idx+1, user[0], user[1])
                _repMessage += "\n\n^(Ben bir botum ve bu eylem otomatik olarak gerçekleştirildi. Kullanılabilecek diğer komutlar için !help veya !yardim ile yanıtlayın.)"
                reply.reply(_repMessage)
            elif checkComment(replyMessage, help) and reply.author != reddit.user.me():
                print("***** Reply To {} *****".format(reply.author))
                _repMessage = "Selam! Yardıma ihtiyacın olduğunu duydum da geldim.\n\n[Bu linke](https://www.reddit.com/user/Rei-Chikita-Bot/comments/17qlilu/reichikitabot_kullan%C4%B1m_rehberi/) tıklayarak komutlar ve botun kullanımı hakkında daha fazla bilgi edinebilirsin.\n\nEğer botun kendisi ile ilgili bilgi almak istiyorsan [buraya](https://www.reddit.com/user/Rei-Chikita-Bot/comments/x4sxmh/merhaba_ben_reichikitabot/) göz atabilirsin.\n\nGörüşürüz 😘"
                reply.reply(_repMessage)
            reply.mark_read()


def mentionCheck():
    for mentions in reddit.inbox.mentions():
        if mentions.new:
            randomImage1 = "https://chikitabot.net/archive/chikita?id=random"
            print("****** Mentioned ******")
            print(mentions.author)
            print(mentions.body)


            chikilib.puan_ekle(mentions.author, 15)


            _mentionMessage = "Merhaba, **" + str(mentions.author) + "**" \
                "! \n\n Görünüşe bakılırsa beni çağırmışsın, senin için buraya bir [Rei fotoğrafı]({}) bıraktım. \n\n Umarım beğenirsin \^-^" \
                " \n\n " + \
                "*** \n" + \
                "^(Ben Bir Botum Ve Bu Eylem Otomatik Olarak Gerçekleştirildi..)" + " \n\n " + \
                "[Bilgi](https://www.reddit.com/user/Rei-Chikita-Bot/comments/x4sxmh/merhaba_ben_reichikitabot/)"

            mentionMessage = _mentionMessage.format(randomImage1)

            mentions.reply(mentionMessage)
            mentions.mark_read()


def main():
    time.sleep(time_sleep)
    subreddit = reddit.subreddit('TaReiKat+ReiChikitaSevenler')

    for gonderi in subreddit.new(limit=10):
        randomImage = "https://chikitabot.net/archive/chikita?id=random"

        _botMesaj = "Merhaba, subumuzda gönderi paylaştığın için teşekkürler!" + "\n\n" + \
            "Buraya senin için rastgele seçilmiş bir [Rei peluş fotoğrafı]({}) bırakıyorum." + \
            " \n\n " + \
            "^(Ben Bir Botum Ve Bu Eylem Otomatik Olarak Gerçekleştirildi..)" + " \n\n " + \
            "[Bilgi](https://www.reddit.com/user/Rei-Chikita-Bot/comments/x4sxmh/merhaba_ben_reichikitabot/)" + " | " + \
            "[Kaynak Kodum](https://github.com/uYazilimciGenc/Rei-Chikita-Bot)"

        botMesaj = _botMesaj.format(randomImage)
        if gonderi.saved != True:
            print("Post title: " + gonderi.title)
            gonderi.upvote()  # Post downvote if wanted to use.
            print('{Bu gönderiye başarı ile upvote atıldı!}')
            gonderi.reply(botMesaj)
            print('\n{Bu Gönderiye Başarı İle Yorum Yapıldı!}')
            chikilib.puan_ekle(gonderi.author, 30)
            print("\n{Gönderi sahibine çikipuan eklendi!}")
            print("****************")
            gonderi.save()


while True:
    try:
        main()
        mentionCheck()
        replyCheck()
    except Exception as e:
        print(str(e) + ", 150 saniyeliğine durduruluyor.")
        time.sleep(150)
