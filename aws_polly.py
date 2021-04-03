import boto3
#connect polly
po = boto3.client('polly')
response=po.synthesize_speech(Text="Hello Aswin,This is AWS Polly service test",OutputFormat='mp3',VoiceId='Joanna')
#create file to store audio
file=open('myaudio.mp3','wb')
file.write(response['AudioStream'].read())
file.close()
#Play audio
import IPython
IPython.display.Audio("myaudio.mp3")