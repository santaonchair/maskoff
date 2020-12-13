from transformers import FillMaskPipeline, AutoModelWithLMHead, AutoTokenizer
from .utils import random_index


class MaskOffPipeline(FillMaskPipeline):
    """
    Masked language modeling prediction pipeline using any `ModelWithLMHead`
    """
    def __init__(self, name="bert-base-uncased", **kwargs):
        super().__init__(
            AutoModelWithLMHead.from_pretrained(name),
            AutoTokenizer.from_pretrained(name),
            **kwargs
        )

    def __call__(self, texts, topk=5, **kwargs):
        """
        Print predicted tokens and scores

        Arguments:
            texts (`str` or `list of str`): One or several texts.
            topk (int): The number of predictions to print
        """
        self.topk = topk

        if isinstance(texts, str):
            texts = [texts]

        for tokens in texts:
            tokens = tokens.split()

            # Replace [MASK] to self.tokenizer.mask_token
            tokens = [self.tokenizer.mask_token if token == "[MASK]" else token for token in tokens]

            # Randomly mask single token if masked token is not given
            if self.tokenizer.mask_token not in tokens:
                masked_ids = random_index(tokens)
                tokens[masked_ids] = self.tokenizer.mask_token

            print(" ".join(tokens))
            for prediction in super().__call__(" ".join(tokens)):
                print("{:<15}{:.2%}".format(prediction['token_str'], prediction['score']))
