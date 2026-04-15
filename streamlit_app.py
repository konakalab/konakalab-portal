import streamlit as st

# ページ設定：ワイドモードにして、ポータル感を出す
st.set_page_config(
    page_title="My Data Portfolio",
    page_icon="🚀",
    layout="wide"
)

# カスタムCSSでカードのデザインを少し整える（オプション）
st.markdown("""
    <style>
    .stButton>button {
        border-radius: 20px;
        height: 3em;
        transition: 0.3s;
    }
    .stButton>button:hover {
        border-color: #ff4b4b;
        color: #ff4b4b;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🌐 My Dashboards Portal")
st.info("私が作成したデータ分析ダッシュボードのアーカイブです。")

st.divider()

# 管理するアプリのリスト
# 新しいアプリを作ったらここに追加するだけでOK
apps = [
    {
        "title": "B.LEAGUE Lineup Analysis",
        "url": "https://bleaguelineupanalysis-fceb7thn6vobjxkzreuhhg.streamlit.app/",
        "description": "🏀 選手の組み合わせによる得失点効率の可視化。ラインナップの相性を分析します。",
        "tag": "Sports"
    },
    {
        "title": "Sample Analysis Project",
        "url": "#", # 実際のURLに置き換え
        "description": "📈 データのトレンド分析と将来予測を行うダッシュボードです。",
        "tag": "Business"
    },
    # 3つ目、4つ目も同様に追加...
]

# 3列構成でカードを並べる
cols = st.columns(3)

for i, app in enumerate(apps):
    with cols[i % 3]:
        # タイトルとタグの表示
        st.caption(f"Category: {app['tag']}")
        st.subheader(app["title"])
        
        # 説明文
        st.write(app["description"])
        
        # リンクボタン
        st.link_button("View App →", app["url"], use_container_width=True)
        
        # カード間の余白
        st.write("\n")

st.divider()
st.caption("© 2024 My Name - Built with Streamlit")
