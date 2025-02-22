def remove_matching_pair(player_cards, available_cards, target_sum):
    for card in player_cards[:]:  
        matching_card = target_sum - card
        if matching_card in available_cards:
            player_cards.remove(card)
            available_cards.remove(matching_card)
            return True
    return False
            
def solution(coin, cards):
    answer = 1  # 첫 번째 라운드는 무조건 진행
    n = len(cards)
    player_hand = cards[:n//3]  # 초기 보유 카드 
    draw_index = n // 3  # 남은 카드에서 가져올 첫 번째 인덱스
    drawn_cards= []  # 뽑은 카드 저장 리스트
    
    while coin >= 0 and draw_index < n - 1:  
        # 뽑을 카드 2장 추가
        drawn_cards.extend(cards[draw_index :draw_index +2]) 

        # 내 카드끼리 짝을 맞출 수 있다면, 그대로 진행
        if remove_matching_pair(player_hand, player_hand, n + 1):
            pass
        # 내 카드와 남은 카드에서 짝을 맞출 수 있으면, 코인 1개를 사용
        elif coin >= 1 and remove_matching_pair(player_hand, drawn_cards, n + 1):
            coin -= 1
        # 남은 카드끼리 짝을 맞출 수 있으면, 코인 2개를 사용
        elif coin >= 2 and remove_matching_pair(drawn_cards, drawn_cards, n + 1):
            coin -= 2
        else:
            break
        
        answer += 1
        draw_index += 2 
    
    return answer