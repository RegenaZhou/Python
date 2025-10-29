class Clock:
    id=None
    price=None

    def ring(self):
        import winsound
        winsound.Beep(200,3000) #winsound.Beep(频率,持续时间)

clock1=Clock()
clock1.id="003032"
clock1.price=19.99
print(f"闹钟ID：{clock1.id}，价格：{clock1.price}")
clock1.ring()

clock2=Clock()
clock2.id="003033"
clock2.price=21.99
print(f"闹钟ID：{clock2.id}，价格：{clock2.price}")
clock2.ring()