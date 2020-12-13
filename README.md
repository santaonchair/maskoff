<h1 align="center">mask off</h1>
<p align="center">
😷 Mask off and Be happy 😙
</p>

<h2 align="center">Description</h2>
This repository shows how MLM works using `FillMaskPipeline` from HuggingFace's `transformers` library.

<h2 align="center">Usage</h2>

Mask off through `MaskOffPipeline`

``` python
>>> from maskoff import MaskOffPipeline

>>> pipeline = MaskOffPipeline()
>>> pipeline("Chase a check (Chase it), never chase a [MASK] (Don't chase no bitches)")
Chase a check (Chase it), never chase a [MASK] (Don't chase no bitches)
check     48.78%
bitch     2.23%
woman     1.44%
girl      1.14%
man       0.67%

```

One random word will be masked If there's no `[MASK]` in text.

``` python
>>> pipeline("Rob the bank, we gon' rob the game (Gang)")
Rob the bank, we gon' rob the [MASK] (Gang)
bank      13.85%
church    2.22%
police    2.19%
banks     2.16%
house     1.78%

```

Use models that have been trained with a masked language modeling objective.

See available models in [here](https://huggingface.co/models?filter=lm-head)

``` python
from maskoff import MaskOffPipeline

# default: `bert-base-uncased`
>>> pipeline = MaskOffPipeline()

>>> pipeline = MaskOffPipeline('roberta-base')
>>> pipeline("I lie without a mask, thus I am an honest man.")
I lie without a mask, thus I am an <mask> man.
Ġinvisible36.82%
Ġold      11.17%
Ġordinary 7.31%
Ġhonest   7.24%
Ġevil     3.17%

>>> pipeline = MaskOffPipeline('albert-large-v2')
>>> pipeline("I lie without a mask, thus I am an honest man.")
I lie without a mask, thus I am an [MASK] man.
▁invisible10.04%
▁immortal 6.74%
▁evil     3.85%
▁honest   3.64%
▁upright  3.34%

```