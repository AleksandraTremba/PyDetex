"""
PyDetex
https://github.com/ppizarror/PyDetex

SYMBOLS
Contain latex commands converted to symbol.
"""

__all__ = [
    'REPLACE_EQUATION_SYMBOLS_LIBRARY',
    'REPLACE_SYMBOLS_LIBRARY',
    'REPLACE_TEX_COMMANDS_LIBRARY'
]

from typing import List, Tuple

REPLACE_SYMBOLS_LIBRARY: List[Tuple[str, str]] = [
    # Common
    ('\\ ', ' '),
    ('\\\\', '\n'),

    # Letters
    ('--', '–'),
    ('---', '—'),
    ('\&', '&'),
    ('~', ' '),
    ('ﬁ', 'fi')
]

REPLACE_EQUATION_SYMBOLS_LIBRARY: List[Tuple[str, str]] = [
    ('^(', '⁽'),
    ('^)', '⁾'),
    ('^+', '⁺'),
    ('^-', '⁻'),
    ('^0', '⁰'),
    ('^1', '¹'),
    ('^2', '²'),
    ('^3', '³'),
    ('^4', '⁴'),
    ('^5', '⁵'),
    ('^6', '⁶'),
    ('^7', '⁷'),
    ('^8', '⁸'),
    ('^9', '⁹'),
    ('^=', '⁼'),
    ('^A', 'ᴬ'),
    ('^a', 'ᵃ'),
    ('^B', 'ᴮ'),
    ('^b', 'ᵇ'),
    ('^c', 'ᶜ'),
    ('^D', 'ᴰ'),
    ('^d', 'ᵈ'),
    ('^E', 'ᴱ'),
    ('^e', 'ᵉ'),
    ('^f', 'ᶠ'),
    ('^G', 'ᴳ'),
    ('^g', 'ᵍ'),
    ('^h', 'ʰ'),
    ('^H', 'ᴴ'),
    ('^I', 'ᴵ'),
    ('^i', 'ⁱ'),
    ('^j', 'ʲ'),
    ('^J', 'ᴶ'),
    ('^K', 'ᴷ'),
    ('^k', 'ᵏ'),
    ('^l', 'ˡ'),
    ('^L', 'ᴸ'),
    ('^M', 'ᴹ'),
    ('^m', 'ᵐ'),
    ('^N', 'ᴺ'),
    ('^n', 'ⁿ'),
    ('^O', 'ᴼ'),
    ('^o', 'ᵒ'),
    ('^P', 'ᴾ'),
    ('^p', 'ᵖ'),
    ('^r', 'ʳ'),
    ('^R', 'ᴿ'),
    ('^s', 'ˢ'),
    ('^T', 'ᵀ'),
    ('^t', 'ᵗ'),
    ('^U', 'ᵁ'),
    ('^u', 'ᵘ'),
    ('^v', 'ᵛ'),
    ('^w', 'ʷ'),
    ('^W', 'ᵂ'),
    ('^x', 'ˣ'),
    ('^y', 'ʸ'),
    ('^z', 'ᶻ'),
    ('_(', '₍'),
    ('_)', '₎'),
    ('_+', '₊'),
    ('_-', '₋'),
    ('_0', '₀'),
    ('_1', '₁'),
    ('_2', '₂'),
    ('_3', '₃'),
    ('_4', '₄'),
    ('_5', '₅'),
    ('_6', '₆'),
    ('_7', '₇'),
    ('_8', '₈'),
    ('_9', '₉'),
    ('_=', '₌'),
    ('_a', 'ₐ'),
    ('_e', 'ₑ'),
    ('_h', 'ₕ'),
    ('_i', 'ᵢ'),
    ('_k', 'ₖ'),
    ('_l', 'ₗ'),
    ('_m', 'ₘ'),
    ('_n', 'ₙ'),
    ('_o', 'ₒ'),
    ('_p', 'ₚ'),
    ('_r', 'ᵣ'),
    ('_s', 'ₛ'),
    ('_t', 'ₜ'),
    ('_u', 'ᵤ'),
    ('_v', 'ᵥ'),
    ('_x', 'ₓ')
]

REPLACE_TEX_COMMANDS_LIBRARY: List[Tuple[str, str]] = [
    ('\\AC', '∿'),
    ('\\aleph', 'ℵ'),
    ('\\alpha', 'α'),
    ('\\amalg', '⨿'),
    ('\\angle', '∠'),
    ('\\approx', '≈'),
    ('\\approxeq', '≊'),
    ('\\asterism', '⁂'),
    ('\\asymp', '≍'),
    ('\\backepsilon', '϶'),
    ('\\backprime', '‵'),
    ('\\backsim', '∽'),
    ('\\backsimeq', '⋍'),
    ('\\barwedge', '⊼'),
    ('\\because', '∵'),
    ('\\beta', 'β'),
    ('\\beth', 'ℶ'),
    ('\\between', '≬'),
    ('\\bigcap', '⋂'),
    ('\\bigcup', '⋃'),
    ('\\bigodot', '⨀'),
    ('\\bigoplus', '⨁'),
    ('\\bigotimes', '⨂'),
    ('\\bigsqcap', '⨅'),
    ('\\bigsqcup', '⨆'),
    ('\\bigvee', '⋁'),
    ('\\bigwedge', '⋀'),
    ('\\bot', '⊥'),
    ('\\bowtie', '⋈'),
    ('\\boxdot', '⊡'),
    ('\\boxminus', '⊟'),
    ('\\boxplus', '⊞'),
    ('\\boxtimes', '⊠'),
    ('\\bullet', '•'),
    ('\\Bumpeq', '≎'),
    ('\\bumpeq', '≏'),
    ('\\cap', '∩'),
    ('\\Cap', '⋒'),
    ('\\cdot', '·'),
    ('\\cdots', '⋯'),
    ('\\checkmark', '✓'),
    ('\\chi', 'χ'),
    ('\\circ', '∘'),
    ('\\circeq', '≗'),
    ('\\circlearrowleft', '↺'),
    ('\\circlearrowright', '↻'),
    ('\\circledast', '⊛'),
    ('\\circledcirc', '⊚'),
    ('\\circleddash', '⊝'),
    ('\\clubsuit', '♣'),
    ('\\coloneqq', '≔'),
    ('\\complement', '∁'),
    ('\\cong', '≅'),
    ('\\coprod', '∐'),
    ('\\copyright', '©'),
    ('\\cup', '∪'),
    ('\\Cup', '⋓'),
    ('\\curlyeqprec', '⋞'),
    ('\\curlyeqsucc', '⋟'),
    ('\\curlyvee', '⋎'),
    ('\\curlywedge', '⋏'),
    ('\\curvearrowleft', '↶'),
    ('\\curvearrowright', '↷'),
    ('\\dagger', '†'),
    ('\\daleth', 'ℸ'),
    ('\\dashleftarrow', '⇠'),
    ('\\dashrightarrow', '⇢'),
    ('\\dashv', '⊣'),
    ('\\dbend', '☡'),
    ('\\ddag', '‡'),
    ('\\ddots', '⋱'),
    ('\\ddot{\\phantom{x}}', '̈'),
    ('\\Delta', 'Δ'),
    ('\\delta', 'δ'),
    ('\\diameter', '⌀'),
    ('\\diamond', '⋄'),
    ('\\diamondsuit', '♢'),
    ('\\Digamma', 'Ϝ'),
    ('\\digamma', 'ϝ'),
    ('\\div', '÷'),
    ('\\divideontimes', '⋇'),
    ('\\doteq', '≐'),
    ('\\doteqdot', '≑'),
    ('\\dotminus', '∸'),
    ('\\dotplus', '∔'),
    ('\\downarrow', '↓'),
    ('\\Downarrow', '⇓'),
    ('\\downdownarrows', '⇊'),
    ('\\downharpoonleft', '⇃'),
    ('\\downharpoonright', '⇂'),
    ('\\ell', 'ℓ'),
    ('\\epsilon', 'ϵ'),
    ('\\eqcirc', '≖'),
    ('\\eqcolon', '∹'),
    ('\\eqqcolon', '≕'),
    ('\\equiv', '≡'),
    ('\\eta', 'η'),
    ('\\Euler', 'ℇ'),
    ('\\euro', '€'),
    ('\\exists', '∃'),
    ('\\fallingdotseq', '≒'),
    ('\\fbox{\\checkmark}', '☑'),
    ('\\fbox{\\phantom{{\\checkmark}}}', '☐'),
    ('\\Finv', 'Ⅎ'),
    ('\\flat', '♭'),
    ('\\forall', '∀'),
    ('\\frac{1}{2}', '½'),
    ('\\frac{1}{3}', '⅓'),
    ('\\frac{1}{4}', '¼'),
    ('\\frac{1}{5}', '⅕'),
    ('\\frac{1}{6}', '⅙'),
    ('\\frac{1}{8}', '⅛'),
    ('\\frac{2}{3}', '⅔'),
    ('\\frac{2}{5}', '⅖'),
    ('\\frac{3}{4}', '¾'),
    ('\\frac{3}{5}', '⅗'),
    ('\\frac{4}{5}', '⅘'),
    ('\\frac{5}{6}', '⅚'),
    ('\\frac{5}{8}', '⅝'),
    ('\\frac{7}{8}', '⅞'),
    ('\\frown', '⌢'),
    ('\\frownie', '☹'),
    ('\\Game', '⅁'),
    ('\\Gamma', 'Γ'),
    ('\\gamma', 'γ'),
    ('\\ge', '≥'),
    ('\\geqq', '≧'),
    ('\\geqslant', '⩾'),
    ('\\gg', '≫'),
    ('\\ggg', '⋙'),
    ('\\gimel', 'ℷ'),
    ('\\gneqq', '≩'),
    ('\\gnsim', '⋧'),
    ('\\gtrdot', '⋗'),
    ('\\gtreqless', '⋛'),
    ('\\gtrless', '≷'),
    ('\\gtrsim', '≳'),
    ('\\guillemotleft', '«'),
    ('\\guillemotright', '»'),
    ('\\guilsinglleft', '‹'),
    ('\\guilsinglright', '›'),
    ('\\hat{\\phantom{x}}', '̂'),
    ('\\hbar', 'ℏ'),
    ('\\heartsuit', '♡'),
    ('\\hookleftarrow', '↩'),
    ('\\hookrightarrow', '↪'),
    ('\\iddots', '⋰'),
    ('\\iiiint', '⨌'),
    ('\\iiint', '∭'),
    ('\\iint', '∬'),
    ('\\Im', 'ℑ'),
    ('\\IM', 'ℑ'),
    ('\\imath', 'ı'),
    ('\\in', '∈'),
    ('\\infty', '∞'),
    ('\\int', '∫'),
    ('\\intercal', '⊺'),
    ('\\invamp', '⅋'),
    ('\\iota', 'ι'),
    ('\\jmath', 'ȷ'),
    ('\\Join', '⨝'),
    ('\\kappa', 'κ'),
    ('\\Koppa', 'Ϟ'),
    ('\\koppa', 'ϟ'),
    ('\\Lambda', 'Λ'),
    ('\\lambda', 'λ'),
    ('\\langle', '〈'),
    ('\\lceil', '⌈'),
    ('\\ldots', '…'),
    ('\\le', '≤'),
    ('\\leftarrow', '←'),
    ('\\Leftarrow', '⇐'),
    ('\\LeftArrowBar', '⇤'),
    ('\\leftarrowtail', '↢'),
    ('\\leftarrowtriangle', '⇽'),
    ('\\leftharpoondown', '↽'),
    ('\\leftharpoonup', '↼'),
    ('\\leftleftarrows', '⇇'),
    ('\\leftrightarrow', '↔'),
    ('\\Leftrightarrow', '⇔'),
    ('\\leftrightarrows', '⇆'),
    ('\\leftrightarrowtriangle', '⇿'),
    ('\\leftrightharpoons', '⇋'),
    ('\\leftrightsquigarrow', '↭'),
    ('\\leftsquigarrow', '⇜'),
    ('\\leftthreetimes', '⋋'),
    ('\\leqq', '≦'),
    ('\\leqslant', '⩽'),
    ('\\lessdot', '⋖'),
    ('\\lesseqgtr', '⋚'),
    ('\\lessgtr', '≶'),
    ('\\lesssim', '≲'),
    ('\\lfloor', '⌊'),
    ('\\lightning', '↯'),
    ('\\ll', '≪'),
    ('\\llangle', '⟪'),
    ('\\llbracket', '〚'),
    ('\\Lleftarrow', '⇚'),
    ('\\lll', '⋘'),
    ('\\ln', '㏑'),
    ('\\lneqq', '≨'),
    ('\\lnsim', '⋦'),
    ('\\log', '㏒'),
    ('\\longleftarrow', '⟵'),
    ('\\longrightarrow', '⟶'),
    ('\\looparrowleft', '↫'),
    ('\\looparrowright', '↬'),
    ('\\Lsh', '↰'),
    ('\\ltimes', '⋉'),
    ('\\mapsfrom', '↤'),
    ('\\mapsto', '↦'),
    ('\\Mapsto', '⇰'),
    ('\\mathbb{0}', '𝟘'),
    ('\\mathbb{1}', '𝟙'),
    ('\\mathbb{2}', '𝟚'),
    ('\\mathbb{3}', '𝟛'),
    ('\\mathbb{4}', '𝟜'),
    ('\\mathbb{5}', '𝟝'),
    ('\\mathbb{6}', '𝟞'),
    ('\\mathbb{7}', '𝟟'),
    ('\\mathbb{8}', '𝟠'),
    ('\\mathbb{9}', '𝟡'),
    ('\\mathbb{\\gamma}', 'ℽ'),
    ('\\mathbb{\\Gamma}', 'ℿ'),
    ('\\mathbb{\\pi}', 'ℼ'),
    ('\\mathbb{\\Pi}', 'ℾ'),
    ('\\mathbb{\\Sigma}', '⅀'),
    ('\\mathbb{A}', '𝔸'),
    ('\\mathbb{a}', '𝕒'),
    ('\\mathbb{B}', '𝔹'),
    ('\\mathbb{b}', '𝕓'),
    ('\\mathbb{C}', 'ℂ'),
    ('\\mathbb{c}', '𝕔'),
    ('\\mathbb{D}', '𝔻'),
    ('\\mathbb{d}', '𝕕'),
    ('\\mathbb{E}', '𝔼'),
    ('\\mathbb{e}', '𝕖'),
    ('\\mathbb{F}', '𝔽'),
    ('\\mathbb{f}', '𝕗'),
    ('\\mathbb{G}', '𝔾'),
    ('\\mathbb{g}', '𝕘'),
    ('\\mathbb{H}', 'ℍ'),
    ('\\mathbb{h}', '𝕙'),
    ('\\mathbb{I}', '𝕀'),
    ('\\mathbb{i}', '𝕚'),
    ('\\mathbb{J}', '𝕁'),
    ('\\mathbb{j}', '𝕛'),
    ('\\mathbb{K}', '𝕂'),
    ('\\mathbb{k}', '𝕜'),
    ('\\mathbb{L}', '𝕃'),
    ('\\mathbb{l}', '𝕝'),
    ('\\mathbb{M}', '𝕄'),
    ('\\mathbb{m}', '𝕞'),
    ('\\mathbb{N}', 'ℕ'),
    ('\\mathbb{n}', '𝕟'),
    ('\\mathbb{O}', '𝕆'),
    ('\\mathbb{o}', '𝕠'),
    ('\\mathbb{P}', 'ℙ'),
    ('\\mathbb{p}', '𝕡'),
    ('\\mathbb{Q}', 'ℚ'),
    ('\\mathbb{q}', '𝕢'),
    ('\\mathbb{R}', 'ℝ'),
    ('\\mathbb{r}', '𝕣'),
    ('\\mathbb{S}', '𝕊'),
    ('\\mathbb{s}', '𝕤'),
    ('\\mathbb{T}', '𝕋'),
    ('\\mathbb{t}', '𝕥'),
    ('\\mathbb{U}', '𝕌'),
    ('\\mathbb{u}', '𝕦'),
    ('\\mathbb{V}', '𝕍'),
    ('\\mathbb{v}', '𝕧'),
    ('\\mathbb{W}', '𝕎'),
    ('\\mathbb{w}', '𝕨'),
    ('\\mathbb{X}', '𝕏'),
    ('\\mathbb{x}', '𝕩'),
    ('\\mathbb{Y}', '𝕐'),
    ('\\mathbb{y}', '𝕪'),
    ('\\mathbb{Z}', 'ℤ'),
    ('\\mathbb{z}', '𝕫'),
    ('\\mathbf{A}', '𝐀'),
    ('\\mathbf{a}', '𝐚'),
    ('\\mathbf{B}', '𝐁'),
    ('\\mathbf{b}', '𝐛'),
    ('\\mathbf{C}', '𝐂'),
    ('\\mathbf{c}', '𝐜'),
    ('\\mathbf{D}', '𝐃'),
    ('\\mathbf{d}', '𝐝'),
    ('\\mathbf{E}', '𝐄'),
    ('\\mathbf{e}', '𝐞'),
    ('\\mathbf{F}', '𝐅'),
    ('\\mathbf{f}', '𝐟'),
    ('\\mathbf{G}', '𝐆'),
    ('\\mathbf{g}', '𝐠'),
    ('\\mathbf{H}', '𝐇'),
    ('\\mathbf{h}', '𝐡'),
    ('\\mathbf{I}', '𝐈'),
    ('\\mathbf{i}', '𝐢'),
    ('\\mathbf{J}', '𝐉'),
    ('\\mathbf{j}', '𝐣'),
    ('\\mathbf{K}', '𝐊'),
    ('\\mathbf{k}', '𝐤'),
    ('\\mathbf{L}', '𝐋'),
    ('\\mathbf{l}', '𝐥'),
    ('\\mathbf{M}', '𝐌'),
    ('\\mathbf{m}', '𝐦'),
    ('\\mathbf{N}', '𝐍'),
    ('\\mathbf{n}', '𝐧'),
    ('\\mathbf{O}', '𝐎'),
    ('\\mathbf{o}', '𝐨'),
    ('\\mathbf{P}', '𝐏'),
    ('\\mathbf{p}', '𝐩'),
    ('\\mathbf{Q}', '𝐐'),
    ('\\mathbf{q}', '𝐪'),
    ('\\mathbf{R}', '𝐑'),
    ('\\mathbf{r}', '𝐫'),
    ('\\mathbf{S}', '𝐒'),
    ('\\mathbf{s}', '𝐬'),
    ('\\mathbf{T}', '𝐓'),
    ('\\mathbf{t}', '𝐭'),
    ('\\mathbf{U}', '𝐔'),
    ('\\mathbf{u}', '𝐮'),
    ('\\mathbf{V}', '𝐕'),
    ('\\mathbf{v}', '𝐯'),
    ('\\mathbf{W}', '𝐖'),
    ('\\mathbf{w}', '𝐰'),
    ('\\mathbf{X}', '𝐗'),
    ('\\mathbf{x}', '𝐱'),
    ('\\mathbf{Y}', '𝐘'),
    ('\\mathbf{y}', '𝐲'),
    ('\\mathbf{Z}', '𝐙'),
    ('\\mathbf{z}', '𝐳'),
    ('\\mathcal B', 'ℬ'),
    ('\\mathcal e', 'ℯ'),
    ('\\mathcal E', 'ℰ'),
    ('\\mathcal F', 'ℱ'),
    ('\\mathcal g', 'ℊ'),
    ('\\mathcal H', 'ℋ'),
    ('\\mathcal I', 'ℐ'),
    ('\\mathcal L', 'ℒ'),
    ('\\mathcal{A}', '𝓐'),
    ('\\mathcal{B}', '𝓑'),
    ('\\mathcal{C}', '𝓒'),
    ('\\mathcal{D}', '𝓓'),
    ('\\mathcal{E}', '𝓔'),
    ('\\mathcal{F}', '𝓕'),
    ('\\mathcal{G}', '𝓖'),
    ('\\mathcal{H}', '𝓗'),
    ('\\mathcal{I}', '𝓘'),
    ('\\mathcal{J}', '𝓙'),
    ('\\mathcal{K}', '𝓚'),
    ('\\mathcal{L}', '𝓛'),
    ('\\mathcal{M}', '𝓜'),
    ('\\mathcal{N}', '𝓝'),
    ('\\mathcal{O}', '𝓞'),
    ('\\mathcal{P}', '𝓟'),
    ('\\mathcal{Q}', '𝓠'),
    ('\\mathcal{R}', '𝓡'),
    ('\\mathcal{S}', '𝓢'),
    ('\\mathcal{T}', '𝓣'),
    ('\\mathcal{U}', '𝓤'),
    ('\\mathcal{V}', '𝓥'),
    ('\\mathcal{W}', '𝓦'),
    ('\\mathcal{X}', '𝓧'),
    ('\\mathcal{Y}', '𝓨'),
    ('\\mathcal{Z}', '𝓩'),
    ('\\mathfrak C', 'ℭ'),
    ('\\mathfrak H', 'ℌ'),
    ('\\mathfrak Z', 'ℨ'),
    ('\\mathfrak{A}', '𝔄'),
    ('\\mathfrak{a}', '𝔞'),
    ('\\mathfrak{B}', '𝔅'),
    ('\\mathfrak{b}', '𝔟'),
    ('\\mathfrak{c}', '𝔠'),
    ('\\mathfrak{D}', '𝔇'),
    ('\\mathfrak{d}', '𝔡'),
    ('\\mathfrak{E}', '𝔈'),
    ('\\mathfrak{e}', '𝔢'),
    ('\\mathfrak{F}', '𝔉'),
    ('\\mathfrak{f}', '𝔣'),
    ('\\mathfrak{G}', '𝔊'),
    ('\\mathfrak{g}', '𝔤'),
    ('\\mathfrak{h}', '𝔥'),
    ('\\mathfrak{i}', '𝔦'),
    ('\\mathfrak{J}', '𝔍'),
    ('\\mathfrak{j}', '𝔧'),
    ('\\mathfrak{K}', '𝔎'),
    ('\\mathfrak{k}', '𝔨'),
    ('\\mathfrak{L}', '𝔏'),
    ('\\mathfrak{l}', '𝔩'),
    ('\\mathfrak{M}', '𝔐'),
    ('\\mathfrak{m}', '𝔪'),
    ('\\mathfrak{N}', '𝔑'),
    ('\\mathfrak{n}', '𝔫'),
    ('\\mathfrak{O}', '𝔒'),
    ('\\mathfrak{o}', '𝔬'),
    ('\\mathfrak{P}', '𝔓'),
    ('\\mathfrak{p}', '𝔭'),
    ('\\mathfrak{Q}', '𝔔'),
    ('\\mathfrak{q}', '𝔮'),
    ('\\mathfrak{r}', '𝔯'),
    ('\\mathfrak{S}', '𝔖'),
    ('\\mathfrak{s}', '𝔰'),
    ('\\mathfrak{T}', '𝔗'),
    ('\\mathfrak{t}', '𝔱'),
    ('\\mathfrak{U}', '𝔘'),
    ('\\mathfrak{u}', '𝔲'),
    ('\\mathfrak{V}', '𝔙'),
    ('\\mathfrak{v}', '𝔳'),
    ('\\mathfrak{W}', '𝔚'),
    ('\\mathfrak{w}', '𝔴'),
    ('\\mathfrak{X}', '𝔛'),
    ('\\mathfrak{x}', '𝔵'),
    ('\\mathfrak{Y}', '𝔜'),
    ('\\mathfrak{y}', '𝔶'),
    ('\\mathfrak{z}', '𝔷'),
    ('\\mathit{A}', '𝐴'),
    ('\\mathit{a}', '𝑎'),
    ('\\mathit{B}', '𝐵'),
    ('\\mathit{b}', '𝑏'),
    ('\\mathit{C}', '𝐶'),
    ('\\mathit{c}', '𝑐'),
    ('\\mathit{D}', '𝐷'),
    ('\\mathit{d}', '𝑑'),
    ('\\mathit{E}', '𝐸'),
    ('\\mathit{e}', '𝑒'),
    ('\\mathit{F}', '𝐹'),
    ('\\mathit{f}', '𝑓'),
    ('\\mathit{G}', '𝐺'),
    ('\\mathit{g}', '𝑔'),
    ('\\mathit{H}', '𝐻'),
    ('\\mathit{h}', '𝘩'),
    ('\\mathit{I}', '𝐼'),
    ('\\mathit{i}', '𝑖'),
    ('\\mathit{J}', '𝐽'),
    ('\\mathit{j}', '𝑗'),
    ('\\mathit{K}', '𝐾'),
    ('\\mathit{k}', '𝑘'),
    ('\\mathit{L}', '𝐿'),
    ('\\mathit{l}', '𝑙'),
    ('\\mathit{M}', '𝑀'),
    ('\\mathit{m}', '𝑚'),
    ('\\mathit{N}', '𝑁'),
    ('\\mathit{n}', '𝑛'),
    ('\\mathit{O}', '𝑂'),
    ('\\mathit{o}', '𝑜'),
    ('\\mathit{P}', '𝑃'),
    ('\\mathit{p}', '𝑝'),
    ('\\mathit{Q}', '𝑄'),
    ('\\mathit{q}', '𝑞'),
    ('\\mathit{R}', '𝑅'),
    ('\\mathit{r}', '𝑟'),
    ('\\mathit{S}', '𝑆'),
    ('\\mathit{s}', '𝑠'),
    ('\\mathit{T}', '𝑇'),
    ('\\mathit{t}', '𝑡'),
    ('\\mathit{U}', '𝑈'),
    ('\\mathit{u}', '𝑢'),
    ('\\mathit{V}', '𝑉'),
    ('\\mathit{v}', '𝑣'),
    ('\\mathit{W}', '𝑊'),
    ('\\mathit{w}', '𝑤'),
    ('\\mathit{X}', '𝑋'),
    ('\\mathit{x}', '𝑥'),
    ('\\mathit{Y}', '𝑌'),
    ('\\mathit{y}', '𝑦'),
    ('\\mathit{Z}', '𝑍'),
    ('\\mathit{z}', '𝑧'),
    ('\\mathring{\\mathrm A}', 'Å'),
    ('\\mathrm K', 'K'),
    ('\\mathrm{d}', 'ⅆ'),
    ('\\mathrsfs B', 'ℬ'),
    ('\\mathrsfs e', 'ℯ'),
    ('\\mathrsfs E', 'ℰ'),
    ('\\mathrsfs F', 'ℱ'),
    ('\\mathrsfs H', 'ℋ'),
    ('\\mathrsfs I', 'ℐ'),
    ('\\mathrsfs L', 'ℒ'),
    ('\\mathscr{A}', '𝒜'),
    ('\\mathscr{C}', '𝒞'),
    ('\\mathscr{D}', '𝒟'),
    ('\\mathscr{G}', '𝒢'),
    ('\\mathscr{J}', '𝒥'),
    ('\\mathscr{K}', '𝒦'),
    ('\\mathscr{M}', 'ℳ'),
    ('\\mathscr{N}', '𝒩'),
    ('\\mathscr{O}', '𝒪'),
    ('\\mathscr{P}', '𝒫'),
    ('\\mathscr{Q}', '𝒬'),
    ('\\mathscr{R}', 'ℛ'),
    ('\\mathscr{S}', '𝒮'),
    ('\\mathscr{T}', '𝒯'),
    ('\\mathscr{U}', '𝒰'),
    ('\\mathscr{V}', '𝒱'),
    ('\\mathscr{W}', '𝒲'),
    ('\\mathscr{X}', '𝒳'),
    ('\\mathscr{Y}', '𝒴'),
    ('\\mathscr{Z}', '𝒵'),
    ('\\measuredangle', '∡'),
    ('\\mho', '℧'),
    ('\\mid', '∣'),
    ('\\models', '⊧'),
    ('\\mp', '∓'),
    ('\\mu', 'μ'),
    ('\\multimap', '⊸'),
    ('\\nabla', '∇'),
    ('\\natural', '♮'),
    ('\\ncong', '≇'),
    ('\\ne', '≠'),
    ('\\nearrow', '↗'),
    ('\\neg', '¬'),
    ('\\nexist', '∄'),
    ('\\ngeq', '≱'),
    ('\\ngtr', '≯'),
    ('\\ni', '∋'),
    ('\\nleftarrow', '↚'),
    ('\\nLeftarrow', '⇍'),
    ('\\nleftrightarrow', '↮'),
    ('\\nLeftrightarrow', '⇎'),
    ('\\nleq', '≰'),
    ('\\nless', '≮'),
    ('\\nmid', '∤'),
    ('\\not\\approx', '≉'),
    ('\\not\\asymp', '≭'),
    ('\\not\\equiv', '≢'),
    ('\\not\\exists', '∄'),
    ('\\not\\gtrless', '≹'),
    ('\\not\\gtrsim', '≵'),
    ('\\not\\lessgtr', '≸'),
    ('\\not\\lesssim', '≴'),
    ('\\not\\preceq', '⋠'),
    ('\\not\\simeq', '≄'),
    ('\\not\\sqsubseteq', '⋢'),
    ('\\not\\sqsupseteq', '⋣'),
    ('\\not\\subset', '⊄'),
    ('\\not\\succeq', '⋡'),
    ('\\not\\supset', '⊅'),
    ('\\not\\triangleleft', '⋪'),
    ('\\not\\trianglelefteq', '⋬'),
    ('\\not\\triangleright', '⋫'),
    ('\\not\\trianglerighteq', '⋭'),
    ('\\not\\vdash', '⊬'),
    ('\\not\\vDash', '⊭'),
    ('\\not\\Vdash', '⊮'),
    ('\\not\\VDash', '⊯'),
    ('\\notin', '∉'),
    ('\\notni', '∌'),
    ('\\nparallel', '∦'),
    ('\\nprec', '⊀'),
    ('\\nrightarrow', '↛'),
    ('\\nRightarrow', '⇏'),
    ('\\nsim', '≁'),
    ('\\nsubseteq', '⊈'),
    ('\\nsucc', '⊁'),
    ('\\nsupseteq', '⊉'),
    ('\\nu', 'ν'),
    ('\\nwarrow', '↖'),
    ('\\odot', '⊙'),
    ('\\oiiint', '∰'),
    ('\\oiint', '∯'),
    ('\\oiintctrclockwise', '∳'),
    ('\\oint', '∮'),
    ('\\ointclockwise', '∲'),
    ('\\Omega', 'Ω'),
    ('\\omega', 'ω'),
    ('\\ominus', '⊖'),
    ('\\oplus', '⊕'),
    ('\\oslash', '⊘'),
    ('\\otimes', '⊗'),
    ('\\overline{0}', '‾'),
    ('\\parallel', '∥'),
    ('\\partial', '∂'),
    ('\\perp', '⟂'),
    ('\\Phi', 'Φ'),
    ('\\phi', 'φ'),
    ('\\Pi', 'Π'),
    ('\\pi', 'π'),
    ('\\pitchfork', '⋔'),
    ('\\pm', '±'),
    ('\\pounds', '£'),
    ('\\prec', '≺'),
    ('\\preccurlyeq', '≼'),
    ('\\preceq', '⪯'),
    ('\\precnsim', '⋨'),
    ('\\precsim', '≾'),
    ('\\prime', '′'),
    ('\\prod', '∏'),
    ('\\Proportion', '∷'),
    ('\\propto', '∝'),
    ('\\Psi', 'Ψ'),
    ('\\psi', 'ψ'),
    ('\\Qoppa', 'Ϙ'),
    ('\\qoppa', 'ϙ'),
    ('\\quotedblbase', '„'),
    ('\\quotesinglbase', '‚'),
    ('\\rangle', '〉'),
    ('\\rceil', '⌉'),
    ('\\Re', 'ℜ'),
    ('\\rfloor', '⌋'),
    ('\\RHD', '‣'),
    ('\\rho', 'ρ'),
    ('\\rightarrow', '→'),
    ('\\Rightarrow', '⇒'),
    ('\\RightArrowBar', '⇥'),
    ('\\rightarrowtail', '↣'),
    ('\\rightarrowtriangle', '⇾'),
    ('\\rightharpoondown', '⇁'),
    ('\\rightharpoonup', '⇀'),
    ('\\rightleftarrows', '⇄'),
    ('\\rightleftharpoons', '⇌'),
    ('\\rightrightarrows', '⇉'),
    ('\\rightsquigarrow', '⇝'),
    ('\\rightthreetimes', '⋌'),
    ('\\risingdotseq', '≓'),
    ('\\rrangle', '⟫'),
    ('\\rrbracket', '〛'),
    ('\\Rrightarrow', '⇛'),
    ('\\Rsh', '↱'),
    ('\\rtimes', '⋊'),
    ('\\Sampi', 'Ϡ'),
    ('\\sampi', 'ϡ'),
    ('\\searrow', '↘'),
    ('\\second', '″'),
    ('\\setminus', '⧵'),
    ('\\sharp', '♯'),
    ('\\Sigma', 'Σ'),
    ('\\sigma', 'σ'),
    ('\\sim', '∼'),
    ('\\simeq', '≃'),
    ('\\smallsetminus', '∖'),
    ('\\smile', '⌣'),
    ('\\smiley', '☺'),
    ('\\spadesuit', '♠'),
    ('\\sphericalangle', '∢'),
    ('\\sqbullet', '∍'),
    ('\\sqcap', '⊓'),
    ('\\sqcup', '⊔'),
    ('\\sqrt[3]{}', '∛'),
    ('\\sqrt[4]{}', '∜'),
    ('\\sqrt{}', '√'),
    ('\\sqsubset', '⊏'),
    ('\\sqsubseteq', '⊑'),
    ('\\sqsubsetneq', '⋤'),
    ('\\sqsupset', '⊐'),
    ('\\sqsupseteq', '⊒'),
    ('\\sqsupsetneq', '⋥'),
    ('\\square', '□'),
    ('\\stackrel{=}{=}', '≣'),
    ('\\stackrel{\\frown}{=}', '≘'),
    ('\\stackrel{\\star}{=}', '≛'),
    ('\\stackrel{\\text{\\tiny ?}}{=}', '≟'),
    ('\\stackrel{\\text{\\tiny def}}{=}', '≝'),
    ('\\stackrel{\\vee}{=}', '≚'),
    ('\\stackrel{\\wedge}{=}', '≙'),
    ('\\star', '∗'),
    ('\\Stigma', 'Ϛ'),
    ('\\stigma', 'ϛ'),
    ('\\subset', '⊂'),
    ('\\Subset', '⋐'),
    ('\\subseteq', '⊆'),
    ('\\subsetneq', '⊊'),
    ('\\succ', '≻'),
    ('\\succccurlyeq', '≽'),
    ('\\succeq', '⪰'),
    ('\\succnsim', '⋩'),
    ('\\succsim', '≿'),
    ('\\sum', '∑'),
    ('\\supset', '⊃'),
    ('\\Supset', '⋑'),
    ('\\supseteq', '⊇'),
    ('\\supsetneq', '⊋'),
    ('\\swarrow', '↙'),
    ('\\tau', 'τ'),
    ('\\textasciimacron', '¯'),
    ('\\textbardbl', '‖'),
    ('\\textbrokenbar', '¦'),
    ('\\textcent', '¢'),
    ('\\textcurrency', '¤'),
    ('\\textdiscount', '⁒'),
    ('\\textestimated', '℮'),
    ('\\textexclamdown', '¡'),
    ('\\textinterrobang', '‽'),
    ('\\textinterrobangdown', '⸘'),
    ('\\textlquill', '⁅'),
    ('\\textmu', 'µ'),
    ('\\textordfeminine', 'ª'),
    ('\\textordmasculine', 'º'),
    ('\\textpertenthousand', '‱'),
    ('\\textperthousand', '‰'),
    ('\\textquestiondown', '¿'),
    ('\\textquotedblleft', '“'),
    ('\\textquotedblright', '”'),
    ('\\textquoteleft', '‘'),
    ('\\textquoteright', '’'),
    ('\\textreferencemark', '※'),
    ('\\textregistered', '®'),
    ('\\textrquill', '⁆'),
    ('\\textsuperscript{1}', '¹'),
    ('\\textsuperscript{2}', '²'),
    ('\\textsuperscript{3}', '³'),
    ('\\textsuperscript{o}', '°'),
    ('\\texttrademark', '™'),
    ('\\textyen', '¥'),
    ('\\therefore', '∴'),
    ('\\Theta', 'Θ'),
    ('\\theta', 'θ'),
    ('\\third', '‴'),
    ('\\times', '×'),
    ('\\top', '⊤'),
    ('\\triangle', '△'),
    ('\\triangleleft', '⊲'),
    ('\\triangleq', '≜'),
    ('\\triangleright', '⊳'),
    ('\\twoheadleftarrow', '↞'),
    ('\\twoheadrightarrow', '↠'),
    ('\\underline{\\phantom{x}}', '̲'),
    ('\\unlhd', '⊴'),
    ('\\unrhd', '⊵'),
    ('\\uparrow', '↑'),
    ('\\Uparrow', '⇑'),
    ('\\updownarrow', '↕'),
    ('\\Updownarrow', '⇕'),
    ('\\updownarrows', '⇅'),
    ('\\upharpoonleft', '↿'),
    ('\\upharpoonright', '↾'),
    ('\\uplus', '⊎'),
    ('\\Upsilon', 'Υ'),
    ('\\upsilon', 'υ'),
    ('\\upuparrows', '⇈'),
    ('\\varepsilon', 'ε'),
    ('\\varkappa', 'ϰ'),
    ('\\varnothing', '∅'),
    ('\\varphi', '𝜑'),
    ('\\varpi', '𝜛'),
    ('\\varrho', '𝜚'),
    ('\\varsigma', 'ς'),
    ('\\vartheta', '𝜗'),
    ('\\vdash', '⊢'),
    ('\\Vdash', '⊩'),
    ('\\VDash', '⊫'),
    ('\\vdots', '⋮'),
    ('\\vee', '∨'),
    ('\\veebar', '⊻'),
    ('\\Vvdash', '⊪'),
    ('\\wedge', '∧'),
    ('\\wp', '℘'),
    ('\\wr', '≀'),
    ('\\Xi', 'Ξ'),
    ('\\xi', 'ξ'),
    ('\\Yup', '⅄'),
    ('\\zeta', 'ζ')
]
