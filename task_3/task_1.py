import requests
from loguru import logger


#######################################################################
#                      Настройки программы
#######################################################################

# URL адреса, на которые будем отправлять запросы
REQUEST_URL_1xx="https://httpstat.us/random/100-103"
REQUEST_URL_2xx="https://httpstat.us/random/200-208"
REQUEST_URL_3xx="https://httpstat.us/random/300-308"
REQUEST_URL_4xx="https://httpstat.us/random/400-431"
REQUEST_URL_5xx="https://httpstat.us/random/500-510"

REQUEST_URL_200="https://httpstat.us/200"

# Время в секундах, за которое должен отработать запрос
TIME_FOR_TIMEOUT=5

#######################################################################


def send_request(
    url: str = REQUEST_URL_200,
    timeout: int = TIME_FOR_TIMEOUT
    ) -> bool:
    """
    Функция для отправки запросов на определённый url
    
    url – адрес url, на который будет отправляться запрос
    timeout – время, за которое должен отработать запрос
    """
    try:
        logger.debug(f"Отправка запроса на адрес: {url}")
        response = requests.get(url, timeout=timeout) # Отправляем запрос
        
        # Проверяем первую цифру ответа наличие ошибочного запроса
        if response.status_code // 100 not in [1, 2, 3]:
            response.raise_for_status() # Вызываем исключительную ситуацию
            
        # Логируем успешные запросы
        logger.info(f"Запрос по url: {url} успешно отработан! | " + \
                    f"Статус код: {response.status_code} | " + \
                    f"Кодировка: {response.encoding} | " + \
                    f"Заголовки ответа: {response.headers} | " + \
                    f"Тело ответа: {response.text} | " + \
                    f"История запросов: {response.history}")
    
    # Обрабатываем все возможные ошибки
    except requests.ConnectTimeout as e:
        print(f"Соединение было прервано. Ошибка: {e}") # Timeout
        
    except requests.HTTPError as e:
        # Ошибка со стороны клиента
        if "Client" in str(e):
            print(f"Произошла ошибка на стороне клиента. Ошибка: {e}")
        # Ошибка со стороны сервера
        elif "Server" in str(e):
            print(f"Произошла ошибка на стороне сервера. Ошибка: {e}")
        # Любая другая ошибка во время выполнения запроса
        else:
            print(f"Произошла ошибка при запросе: {e}")
    
    except Exception as e:
        # Любая другая ошибка во время выполнения программы
        print(f"Произошла ошибка при выполнении программы: {e}")


#######################################################################
#                               Запросы
#######################################################################

send_request(REQUEST_URL_1xx, 1)
send_request(REQUEST_URL_2xx)
send_request(REQUEST_URL_3xx)
send_request(REQUEST_URL_4xx)
send_request(REQUEST_URL_5xx)

#######################################################################