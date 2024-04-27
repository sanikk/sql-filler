# Notes on tkinter styles

s = ttk.Style()
s.element_options('TButton')
- shows available options

tk.Frame default style 'Frame'

ttk.Frame default style 'Tframe'
[('Frame.border', {'sticky': 'nswe'})]
('background', 'borderwidth', 'relief')

ttk.Label default style 'TLabel'
layout:
[('Label.border', {'sticky': 'nswe', 
                   'border': '1', 
                   'children': [
                        ('Label.padding', {'sticky': 'nswe', 
                                            'border': '1', 
                                            'children': [
                                                ('Label.label', {'sticky': 'nswe'})
]})]})]
### s.element_names()
('label', '', 'focus', 'treearea', 'separator', 'image', 'arrow', 'downarrow', 'Menubutton.indicator', 
'Treeitem.row', 'vsash', 'text', 'sizegrip', 'indicator', 'Treeheading.cell', 'leftarrow', 'border', 
'Radiobutton.indicator', 'hsash', 'vseparator', 'fill', 'thumb', 'background', 'uparrow', 
'hseparator', 'trough', 'rightarrow', 'Treeitem.indicator', 'slider', 'field', 'pbar', 
'Checkbutton.indicator', 'textarea', 'client', 'tab', 'padding')

### s.configure('.')
{'font': 'TkDefaultFont', 'selectforeground': '#ffffff', 'lightcolor': '#eeebe7', 
'foreground': 'black', 'selectbackground': '#4a6984', 'troughcolor': '#bab5ab', 
'background': '#dcdad5', 'darkcolor': '#cfcdc8', 'bordercolor': '#9e9a91', 'selectborderwidth': 0}

### s.element_options('focus')
('focuscolor', 'focusthickness')

### s.elements_options('label)
('compound', 'space', 'text', 'font', 'foreground', 'underline', 'width', 'anchor', 'justify', 
'wraplength', 'embossed', 'image', 'stipple', 'background')
