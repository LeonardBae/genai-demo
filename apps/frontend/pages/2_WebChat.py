import os
import streamlit as st
import streamlit.components.v1 as components

# From here down is all the StreamLit UI.
st.set_page_config(page_title="GPT Smart Agent", page_icon="📖", layout="wide")
# Add custom CSS styles to adjust padding
st.markdown("""
        <style>
               .block-container {
                    padding-top: 1rem;
                    padding-bottom: 0rem;
                }
        </style>
        """, unsafe_allow_html=True)

with st.sidebar:
    st.markdown("""# Instructions""")
    st.markdown("""

이 Chatbot은 독립적인 Backend Azure Web App에서 호스팅되며 봇 프레임워크 SDK를 사용하여 만들어졌습니다.
(봇 인터페이스는 Azure에서 호스팅되는 Bot Service 앱의 창일 뿐입니다.)

다음의 도구/플러그인을 이용할 수 있습니다.

- 일반적인 지식을 위한 ChatGPT (***use @chatgpt in your question***)
- Azure 특정 서비스 문서의 지식 검색 - Azure Storage Account (***use @docsearch in your question***)
- 책에 대한 지식을 검색 - 3 PDF books (***use @booksearch in your question***)

참고: @로 시작하는 도구 이름을 사용하지 않으면 봇이 자체 지식이나 사용 가능한 도구를 사용하여 질문에 답변하려고 시도합니다.


질문 예시.

- Hello, my name is Bob, what's yours?
- @chatgpt, How do I cook a chocolate cake?
- @booksearch, what normally rich dad do that is different from poor dad?
- @docsearch, Why Covid doesn't affect kids that much compared to adults?
- @docsearch, List the authors that talk about Boosting Algorithms
- Please tell me a joke
    """)
    
st.markdown("""
        <style>
               .block-container {
                    padding-top: 1rem;
                    padding-bottom: 0rem;
                }
        </style>
        """, unsafe_allow_html=True)


BOT_DIRECTLINE_SECRET_KEY = os.environ.get("BOT_DIRECTLINE_SECRET_KEY")

components.html(
f"""
<html>
  <head>
    <script
      crossorigin="anonymous"
      src="https://cdn.botframework.com/botframework-webchat/latest/webchat.js"
    ></script>
    <script crossorigin="anonymous" src="https://unpkg.com/markdown-it@10.0.0/dist/markdown-it.min.js"></script>
     <style>
      html,
      body {{
          height: 100%;
          background-image: linear-gradient( #343541,#525468);
          color: antiquewhite;
          font-family: 'Segoe UI', Calibri, sans-serif;
      }}

      body {{
        padding-left: 5px;
      }}

      #webchat {{
        height: 85%;
        width: 100%;
      }}
      .webchat__stacked-layout--from-user{{
        background-color: rgba(32,33,35, .2);
      }}
      
    </style>
  </head>
  <body>
    <h1><img src='https://blobstorageo4edtammb3b6o.blob.core.windows.net/icon/SK Logo.png' height="40">Smart ChatBot Demo</h1> 
    <div id="webchat" role="main"></div>
    <script>
      // Set  the CSS rules.
      const styleSet = window.WebChat.createStyleSet({{
          bubbleBackground: 'transparent',
          bubbleBorderColor: 'darkslategrey',
          bubbleBorderRadius: 5,
          bubbleBorderStyle: 'solid',
          bubbleBorderWidth: 0,
          bubbleTextColor: 'antiquewhite',

          userAvatarBackgroundColor: 'rgba(53, 55, 64, .3)',
          bubbleFromUserBackground: 'transparent', 
          bubbleFromUserBorderColor: '#E6E6E6',
          bubbleFromUserBorderRadius: 5,
          bubbleFromUserBorderStyle: 'solid',
          bubbleFromUserBorderWidth: 0,
          bubbleFromUserTextColor: 'antiquewhite',

          notificationText: 'white',

          bubbleMinWidth: 400,
          bubbleMaxWidth: 720,

          botAvatarBackgroundColor: 'antiquewhite',
          avatarBorderRadius: 2,
          avatarSize: 40,

          rootHeight: '100%',
          rootWidth: '100%',
          backgroundColor: 'rgba(70, 130, 180, .2)',

          hideUploadButton: 'true'
      }});
      // After generated, you can modify the CSS rules.
      // Change font family and weight. 
      styleSet.textContent = {{
          ...styleSet.textContent,
          fontWeight: 'regular'
      }};

      // Set the avatar options. 
      const avatarOptions = {{
          botAvatarInitials: '.',
          userAvatarInitials: 'Me',
          botAvatarImage: 'https://dwglogo.com/wp-content/uploads/2019/03/1600px-OpenAI_logo-1024x705.png',
          
          }};
      const markdownIt = window.markdownit({{html:true}});
      window.WebChat.renderWebChat(
        {{
          directLine: window.WebChat.createDirectLine({{
            token: '{BOT_DIRECTLINE_SECRET_KEY}'
          }}),
          renderMarkdown: markdownIt.render.bind(markdownIt),
          styleSet, styleOptions: avatarOptions,
          locale: 'en-US'
        }},
        document.getElementById('webchat')
      );
    </script>
  </body>
</html>
""", height=800)