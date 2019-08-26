{"filter":false,"title":"forms.py","tooltip":"/todos/forms.py","undoManager":{"mark":50,"position":50,"stack":[[{"start":{"row":0,"column":0},"end":{"row":8,"column":33},"action":"insert","lines":["from django import forms","from .models import Item","","","class ItemForm(forms.ModelForm):","","    class Meta:","        model = Item","        fields = ('name', 'done')"],"id":1}],[{"start":{"row":8,"column":33},"end":{"row":9,"column":0},"action":"insert","lines":["",""],"id":2},{"start":{"row":9,"column":0},"end":{"row":9,"column":8},"action":"insert","lines":["        "]},{"start":{"row":9,"column":8},"end":{"row":10,"column":0},"action":"insert","lines":["",""]},{"start":{"row":10,"column":0},"end":{"row":10,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":10,"column":4},"end":{"row":10,"column":8},"action":"remove","lines":["    "],"id":3},{"start":{"row":10,"column":0},"end":{"row":10,"column":4},"action":"remove","lines":["    "]}],[{"start":{"row":8,"column":32},"end":{"row":8,"column":33},"action":"insert","lines":[","],"id":4}],[{"start":{"row":8,"column":33},"end":{"row":8,"column":34},"action":"insert","lines":[" "],"id":5}],[{"start":{"row":8,"column":34},"end":{"row":8,"column":36},"action":"insert","lines":["''"],"id":6}],[{"start":{"row":8,"column":35},"end":{"row":8,"column":36},"action":"insert","lines":["o"],"id":7},{"start":{"row":8,"column":36},"end":{"row":8,"column":37},"action":"insert","lines":["n"]}],[{"start":{"row":8,"column":35},"end":{"row":8,"column":37},"action":"remove","lines":["on"],"id":8},{"start":{"row":8,"column":35},"end":{"row":8,"column":42},"action":"insert","lines":["ongoing"]}],[{"start":{"row":8,"column":42},"end":{"row":8,"column":43},"action":"insert","lines":[","],"id":9}],[{"start":{"row":8,"column":43},"end":{"row":8,"column":44},"action":"insert","lines":[" "],"id":10}],[{"start":{"row":8,"column":44},"end":{"row":8,"column":45},"action":"remove","lines":["'"],"id":11},{"start":{"row":8,"column":43},"end":{"row":8,"column":44},"action":"remove","lines":[" "]},{"start":{"row":8,"column":42},"end":{"row":8,"column":43},"action":"remove","lines":[","]}],[{"start":{"row":8,"column":42},"end":{"row":8,"column":43},"action":"insert","lines":["'"],"id":12},{"start":{"row":8,"column":43},"end":{"row":8,"column":44},"action":"insert","lines":[","]}],[{"start":{"row":8,"column":44},"end":{"row":8,"column":46},"action":"insert","lines":["''"],"id":13}],[{"start":{"row":8,"column":45},"end":{"row":8,"column":58},"action":"insert","lines":[" completed_at"],"id":14}],[{"start":{"row":8,"column":32},"end":{"row":8,"column":58},"action":"remove","lines":[", 'ongoing',' completed_at"],"id":15}],[{"start":{"row":8,"column":31},"end":{"row":8,"column":33},"action":"remove","lines":["''"],"id":16}],[{"start":{"row":8,"column":31},"end":{"row":8,"column":32},"action":"insert","lines":["'"],"id":17}],[{"start":{"row":8,"column":32},"end":{"row":8,"column":58},"action":"insert","lines":[", 'ongoing',' completed_at"],"id":18}],[{"start":{"row":8,"column":58},"end":{"row":8,"column":59},"action":"insert","lines":["'"],"id":19}],[{"start":{"row":8,"column":59},"end":{"row":8,"column":60},"action":"insert","lines":[","],"id":20}],[{"start":{"row":8,"column":60},"end":{"row":8,"column":61},"action":"insert","lines":[" "],"id":21},{"start":{"row":8,"column":61},"end":{"row":8,"column":62},"action":"insert","lines":["c"]},{"start":{"row":8,"column":62},"end":{"row":8,"column":63},"action":"insert","lines":["a"]},{"start":{"row":8,"column":63},"end":{"row":8,"column":64},"action":"insert","lines":["r"]}],[{"start":{"row":8,"column":63},"end":{"row":8,"column":64},"action":"remove","lines":["r"],"id":22}],[{"start":{"row":8,"column":63},"end":{"row":8,"column":64},"action":"insert","lines":["t"],"id":23}],[{"start":{"row":8,"column":64},"end":{"row":8,"column":65},"action":"insert","lines":["e"],"id":24},{"start":{"row":8,"column":65},"end":{"row":8,"column":66},"action":"insert","lines":["g"]},{"start":{"row":8,"column":66},"end":{"row":8,"column":67},"action":"insert","lines":["o"]},{"start":{"row":8,"column":67},"end":{"row":8,"column":68},"action":"insert","lines":["r"]},{"start":{"row":8,"column":68},"end":{"row":8,"column":69},"action":"insert","lines":["i"]},{"start":{"row":8,"column":69},"end":{"row":8,"column":70},"action":"insert","lines":["e"]},{"start":{"row":8,"column":70},"end":{"row":8,"column":71},"action":"insert","lines":["s"]}],[{"start":{"row":8,"column":71},"end":{"row":8,"column":72},"action":"insert","lines":["'"],"id":25}],[{"start":{"row":8,"column":61},"end":{"row":8,"column":62},"action":"insert","lines":["'"],"id":26}],[{"start":{"row":8,"column":71},"end":{"row":8,"column":72},"action":"remove","lines":["s"],"id":27},{"start":{"row":8,"column":70},"end":{"row":8,"column":71},"action":"remove","lines":["e"]},{"start":{"row":8,"column":69},"end":{"row":8,"column":70},"action":"remove","lines":["i"]}],[{"start":{"row":8,"column":69},"end":{"row":8,"column":70},"action":"insert","lines":["y"],"id":28}],[{"start":{"row":8,"column":71},"end":{"row":8,"column":72},"action":"insert","lines":[","],"id":29}],[{"start":{"row":8,"column":72},"end":{"row":8,"column":73},"action":"insert","lines":[" "],"id":30},{"start":{"row":8,"column":73},"end":{"row":8,"column":74},"action":"insert","lines":["t"]},{"start":{"row":8,"column":74},"end":{"row":8,"column":75},"action":"insert","lines":["a"]},{"start":{"row":8,"column":75},"end":{"row":8,"column":76},"action":"insert","lines":["g"]},{"start":{"row":8,"column":76},"end":{"row":8,"column":77},"action":"insert","lines":["'"]}],[{"start":{"row":8,"column":73},"end":{"row":8,"column":74},"action":"insert","lines":["'"],"id":31}],[{"start":{"row":8,"column":77},"end":{"row":8,"column":78},"action":"insert","lines":["s"],"id":32}],[{"start":{"row":8,"column":71},"end":{"row":8,"column":79},"action":"remove","lines":[", 'tags'"],"id":33}],[{"start":{"row":8,"column":71},"end":{"row":8,"column":72},"action":"insert","lines":[","],"id":34}],[{"start":{"row":8,"column":72},"end":{"row":8,"column":73},"action":"insert","lines":[" "],"id":35},{"start":{"row":8,"column":73},"end":{"row":8,"column":74},"action":"insert","lines":["t"]},{"start":{"row":8,"column":74},"end":{"row":8,"column":75},"action":"insert","lines":["a"]},{"start":{"row":8,"column":75},"end":{"row":8,"column":76},"action":"insert","lines":["g"]},{"start":{"row":8,"column":76},"end":{"row":8,"column":77},"action":"insert","lines":["s"]}],[{"start":{"row":8,"column":76},"end":{"row":8,"column":77},"action":"remove","lines":["s"],"id":36},{"start":{"row":8,"column":75},"end":{"row":8,"column":76},"action":"remove","lines":["g"]},{"start":{"row":8,"column":74},"end":{"row":8,"column":75},"action":"remove","lines":["a"]},{"start":{"row":8,"column":73},"end":{"row":8,"column":74},"action":"remove","lines":["t"]}],[{"start":{"row":8,"column":73},"end":{"row":8,"column":75},"action":"insert","lines":["''"],"id":37}],[{"start":{"row":8,"column":74},"end":{"row":8,"column":75},"action":"insert","lines":["t"],"id":38},{"start":{"row":8,"column":75},"end":{"row":8,"column":76},"action":"insert","lines":["a"]},{"start":{"row":8,"column":76},"end":{"row":8,"column":77},"action":"insert","lines":["g"]},{"start":{"row":8,"column":77},"end":{"row":8,"column":78},"action":"insert","lines":["s"]}],[{"start":{"row":8,"column":45},"end":{"row":8,"column":46},"action":"remove","lines":[" "],"id":39}],[{"start":{"row":8,"column":32},"end":{"row":8,"column":78},"action":"remove","lines":[", 'ongoing','completed_at', 'category', 'tags'"],"id":40}],[{"start":{"row":10,"column":0},"end":{"row":10,"column":46},"action":"insert","lines":[", 'ongoing','completed_at', 'category', 'tags'"],"id":41}],[{"start":{"row":10,"column":0},"end":{"row":10,"column":2},"action":"insert","lines":["# "],"id":42}],[{"start":{"row":10,"column":2},"end":{"row":10,"column":48},"action":"remove","lines":[", 'ongoing','completed_at', 'category', 'tags'"],"id":43}],[{"start":{"row":8,"column":32},"end":{"row":8,"column":78},"action":"insert","lines":[", 'ongoing','completed_at', 'category', 'tags'"],"id":44}],[{"start":{"row":8,"column":78},"end":{"row":8,"column":79},"action":"insert","lines":[","],"id":45}],[{"start":{"row":8,"column":79},"end":{"row":8,"column":80},"action":"insert","lines":[" "],"id":46}],[{"start":{"row":8,"column":80},"end":{"row":8,"column":82},"action":"insert","lines":["''"],"id":47}],[{"start":{"row":8,"column":81},"end":{"row":8,"column":82},"action":"insert","lines":["A"],"id":48}],[{"start":{"row":8,"column":81},"end":{"row":8,"column":82},"action":"remove","lines":["A"],"id":49}],[{"start":{"row":8,"column":81},"end":{"row":8,"column":82},"action":"insert","lines":["a"],"id":50},{"start":{"row":8,"column":82},"end":{"row":8,"column":83},"action":"insert","lines":["r"]},{"start":{"row":8,"column":83},"end":{"row":8,"column":84},"action":"insert","lines":["r"]},{"start":{"row":8,"column":84},"end":{"row":8,"column":85},"action":"insert","lines":["o"]},{"start":{"row":8,"column":85},"end":{"row":8,"column":86},"action":"insert","lines":["w"]}],[{"start":{"row":8,"column":81},"end":{"row":8,"column":86},"action":"remove","lines":["arrow"],"id":51},{"start":{"row":8,"column":81},"end":{"row":8,"column":82},"action":"insert","lines":["a"]},{"start":{"row":8,"column":82},"end":{"row":8,"column":83},"action":"insert","lines":["s"]},{"start":{"row":8,"column":83},"end":{"row":8,"column":84},"action":"insert","lines":["s"]},{"start":{"row":8,"column":84},"end":{"row":8,"column":85},"action":"insert","lines":["i"]},{"start":{"row":8,"column":85},"end":{"row":8,"column":86},"action":"insert","lines":["g"]},{"start":{"row":8,"column":86},"end":{"row":8,"column":87},"action":"insert","lines":["n"]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":8,"column":87},"end":{"row":8,"column":87},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1565171360366,"hash":"3b205be082475e4e0eceafac333ffb6321cca7fa"}