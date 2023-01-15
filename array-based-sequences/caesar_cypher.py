class CaesarCipher:
    """Class for doing encryption and decryption using the Caesar cipher."""

    def __init__(self, shift: int):
        """Construct Caesar cipher using given integer shift for rotation."""
        encoder = [None] * 26
        decoder = [None] * 26
        for k in range(26):
            encoder[k] = chr((k + shift) % 26 + ord('A'))
            decoder[k] = chr((k - shift) % 26 + ord('A'))
        self._forward = ''.join(encoder)
        self._backward = ''.join(decoder)

    def encrypt(self, message: str):
        """Return string representing encrypted message."""
        return self._transform(message, self._forward)

    def decrypt(self, secret: str):
        """Return decrypted message given encrypted secret."""
        return self._transform(secret, self._backward)

    def _transform(self, original: str, code: str):
        """Utility to perform transformation based on given code string."""
        msg = list(original)
        for v in range(len(msg)):
            if msg[v].isupper():
                j = ord(msg[v]) - ord('A')
                msg[v] = code[j]
        return ''.join(msg)


if __name__ == "__main__":
    cipher = CaesarCipher(3)
    message = "THE EAGLE IS IN PLAY; MEET AT JOE'S"
    coded = cipher.encrypt(message)
    print(f'Secret: {coded}')
    answer = cipher.decrypt(coded)
    print(f'Message: {answer}')
