from kivy.app import App
from kivy.uix.modalview import ModalView
from kivy.clock import Clock
from android.runnable import run_on_ui_thread
from jnius import autoclass

# استدعاء أدوات الأندرويد لتشغيل الـ WebView
WebView = autoclass('android.webkit.WebView')
WebViewClient = autoclass('android.webkit.WebViewClient')
Activity = autoclass('org.kivy.android.PythonActivity').mActivity

class MyWebView(ModalView):
    def __init__(self, **kwargs):
        super(MyWebView, self).__init__(**kwargs)
        self.size_hint = (1, 1)
        self.auto_dismiss = False
        Clock.schedule_once(self.create_webview, 0)

    @run_on_ui_thread
    def create_webview(self, *args):
        webview = WebView(Activity)
        webview.getSettings().setJavaScriptEnabled(True)
        webview.getSettings().setDomStorageEnabled(True)
        webview.setWebViewClient(WebViewClient())
        
        # تشغيل ملف index.html المحرك المحلي داخل الأندرويد
        webview.loadUrl("file:///android_asset/index.html")
        Activity.setContentView(webview)

class MainApp(App):
    def build(self):
        view = MyWebView()
        return view

if __name__ == '__main__':
    MainApp().run()
