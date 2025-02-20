def solution(coin, cards):
    ans = 1
    n = len(cards)
    my_card = cards[:n // 3] # 뽑을 카드 뭉치에 n // 3 개만 내 카드
    draw_index = n // 3 # 라운드 별로 뽑을 카드에 시작 인덱스
    drawn_cards= []
    
    while coin >= 0 and draw_index < n - 1:
        drawn_cards.extend(cards[draw_index :draw_index +2])
        
        if possible(my_card, my_card, n + 1):
            ans += 1
            print("my_card", my_card)
        elif possible(my_card, drawn_cards, n + 1) and coin >= 1:
            coin -= 1
            ans += 1
        elif possible(drawn_cards, drawn_cards, n + 1) and coin >= 2:
            coin -= 2
            ans += 1
        else:
            break
            
        draw_index += 2
        
    return ans

def possible(mycard, pluscard, t):
    for card in mycard[:]:
        tc = t - card
        if tc in pluscard:
            mycard.remove(card)
            pluscard.remove(tc)
            return True
    return False