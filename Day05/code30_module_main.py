import code29_module_name                           # 부르면 이름이 메인이 아니라 본인이름으로 변경

print(f'code30_module_name : {__name__}')

# C int main(void)와 동일
if __name__ == '__main__':                          
        print('main을 실행합니다.')