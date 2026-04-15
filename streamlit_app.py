import streamlit as st

# ページ設定：ワイドモードにして、ポータル感を出す
st.set_page_config(
    page_title="konakalab's Dashboards Portal",
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

st.title("🌐 konakalab's Dashboards Portal")
st.info("konakalabが作成したデータ分析ダッシュボードのポータルサイトです。")

st.divider()

# 管理するアプリのリスト
# 新しいアプリを作ったらここに追加するだけでOK
apps = [
    {
        "title": "B.LEAGUE Lineup Analysis",
        "url": "https://bleaguelineupanalysis-fceb7thn6vobjxkzreuhhg.streamlit.app/",
        "description": "🏀 Play-by-playデータに基づく選手・ラインナップ評価のダッシュボードです",
        "tag": "バスケットボール"
    },
    {
        "title": " 非公式Jリーグ王座(Unofficial Football J-League Champion, UFJC) 歴代ランキング",
        "url": "https://ufjc-konakalab.streamlit.app/", # 実際のURLに置き換え
        "description": "⚽ 「勝利で王者が移動する」をJリーグ開幕から追いかけるダッシュボードです",
        "tag": "サッカー"
    },
    {
        "title": " FIFAワールドカップ2026予測",
        "url": "https://fifawc2026prediction-konakalab.streamlit.app/", # 実際のURLに置き換え
        "description": "⚽ FIFAワールドカップの統計予測モデルの予測結果を公開します",
        "tag": "サッカー"
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
st.caption("© 2026 konakalab - Built with Streamlit")
