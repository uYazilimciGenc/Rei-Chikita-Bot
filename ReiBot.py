import praw
import reiLinks
import random
import time

reddit = praw.Reddit(
    client_id="",  # API Client ID Goes Here
    client_secret="",  # Client Secret Code Goes Here
    user_agent="",  # Define an user agent
    username="",  # Username
    password=""  # Password
)


print("**************** Program Started ****************")


def replyCheck():
    time.sleep(1)
    for reply in reddit.inbox.comment_replies():
        if reply.new:
            print("****** Replied ******")
            print(reply.author)
            print(reply.body)

            replyMessage = reply.body.lower()

            _repMessage = ""

            if "merhaba" in replyMessage and reply.author == "YazilimciGenc" and reply.author != reddit.user.me():
                print("***** Replying *****")
                _repMessage = "Merhaba " + str(reply.author) + "!"
                reply.reply(_repMessage)

            elif ("sağol" in replyMessage or " tşk" in replyMessage or "eyw" in replyMessage or "teşekkürler" in replyMessage or "tesekkurler" in replyMessage or "sagol" in replyMessage) and reply.author != reddit.user.me():
                print("***** Replying *****")
                _repMessage = "Bişi diğil \^^"
                reply.reply(_repMessage)
            elif ("good bot" in replyMessage or "iyi bot" in replyMessage) and reply.author != reddit.user.me():
                print("***** Replying *****")
                _repMessage = "Teşekkürler! Ben de senin iyi olduğunu düşünüyorum :)"
                reply.reply(_repMessage)
            elif ("günaydın" in replyMessage or "gunaydın" in replyMessage or "gunaydin" in replyMessage) and reply.author != reddit.user.me():
                print("***** Replying *****")
                _repMessage = "Sana da günaydın <3"
                reply.reply(_repMessage)
            elif ("iyi geceler" in replyMessage or "iyi aksamlar" in replyMessage or "iyi akşamlar" in replyMessage or "ıyi geceler" in replyMessage or "ıyi akşamlar" in replyMessage or "ıyi aksamlar" in replyMessage) and reply.author != reddit.user.me():
                print("***** Replying *****")
                _repMessage = "Sana da iyi geceler <3"
                reply.reply(_repMessage)
            elif ("seni seviyorum" in replyMessage) and reply.author != reddit.user.me():
                print("***** Replying *****")
                _repMessage = "Ben de seni seviyorum " + \
                    str(reply.author) + " \^^"
                reply.reply(_repMessage)
            elif ("nasılsın" in replyMessage or "nasilsin" in replyMessage or "keyfin nasıl" in replyMessage) and reply.author != reddit.user.me():
                print("***** Replying *****")
                _repMessage = "İyiyim, umarım sen de iyisindir! \^_^"
                reply.reply(_repMessage)
            reply.mark_read()
            print("****")


def mentionCheck():
    for mentions in reddit.inbox.mentions():
        if mentions.new:
            randomImage1 = random.choice(reiLinks.linkArr)
            print("****** Mentioned ******")
            print(mentions.author)
            print(mentions.body)

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
    time.sleep(1)
    subreddit = reddit.subreddit('TaReiKat+ReiChikitaSevenler')

    for gonderi in subreddit.new(limit=10):
        randomImage = random.choice(reiLinks.linkArr)

        print(
            "********* Şu anda veritabanında {} fotoğraf var. *********".format(len(reiLinks.linkArr)))

        _botMesaj = "Merhaba, subumuzda gönderi paylaştığın için teşekkürler!" + "\n\n" + \
            "Buraya senin için rastgele seçilmiş bir [Rei peluş fotoğrafı]({}) bırakıyorum, küçük bir ihtimal ile de normal Rei fotoğrafı var." + \
            " \n\n " + \
            "^(Ben Bir Botum Ve Bu Eylem Otomatik Olarak Gerçekleştirildi..)" + " \n\n " + \
            "[Bilgi](https://www.reddit.com/user/Rei-Chikita-Bot/comments/x4sxmh/merhaba_ben_reichikitabot/)"

        botMesaj = _botMesaj.format(randomImage)
        print("******* Title : " + gonderi.title + " ********")
        if gonderi.saved != True:
            print("Post title: " + gonderi.title)
            gonderi.upvote()  # Post downvote if wanted to use.
            print('{Bu gönderiye başarı ile upvote atıldı!}')
            gonderi.reply(botMesaj)
            print('\n{Bu Gönderiye Başarı İle Yorum Yapıldı!}')
            print("****************")
            gonderi.save()
            print("İşlem yapıldı.")
        else:
            print("Zaten bu gönderiye yorum yapılmış.")


while True:
    try:
        main()
        mentionCheck()
        replyCheck()
    except Exception as e:
        print(str(e) + ", 150 saniyeliğine durduruluyor.")
        time.sleep(150)
