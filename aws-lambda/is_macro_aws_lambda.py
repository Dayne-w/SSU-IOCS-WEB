import json
import numpy as np

def lambda_handler(event, context):
    # POST 메서드로 전달된 데이터 파싱
    try:
        # event['body']에서 x, y 좌표 추출
        body = json.loads(event['body'])

        x = np.array(body['x'], dtype=float)
        y = np.array(body['y'], dtype=float)

        if len(x) > 2 and len(y) > 2:
            # Function to estimate derivatives using central difference method
            def derivative(x):
                dx = np.zeros_like(x)
                dx[1:-1] = (x[2:] - x[:-2]) / 2  # Central difference
                dx[0] = x[1] - x[0]  # Forward difference for the first element
                dx[-1] = x[-1] - x[-2]  # Backward difference for the last element
                return dx

            # First and second derivatives
            x_prime = derivative(x)
            y_prime = derivative(y)
            x_double_prime = derivative(x_prime)
            y_double_prime = derivative(y_prime)

            # Calculating curvature for each point
            # x_prime과 y_prime이 동시에 0인 경우 에러 발생
            valid_indices = (x_prime != 0) | (y_prime != 0)  # x_prime과 y_prime이 동시에 0이 아닌 경우
            curvature = np.abs(
                x_prime[valid_indices] * y_double_prime[valid_indices] - y_prime[valid_indices] * x_double_prime[
                    valid_indices]) / (
                                x_prime[valid_indices] ** 2 + y_prime[valid_indices] ** 2) ** 1.5

            if len(curvature) > 0:
                # Display the curvature values
                mean_curvature = np.mean(curvature)
                max_curvature = np.max(curvature)
                min_curvature = np.min(curvature)
                std_curvature = np.std(curvature)

                isMacro = True if max_curvature <= 0.01 else False

                response = {
                    'statusCode': 200,
                    'body': json.dumps({
                        'isMacro': isMacro,
                        'values': {
                            'MeanCurvature': f"{mean_curvature:.10f}",
                            'MaxCurvature': f"{max_curvature:.10f}",
                            'MinCurvature': f"{min_curvature:.10f}",
                            'CurvatureStd': f"{std_curvature:.10f}"
                        }
                    })
                }

            else:
                response = {
                    'statusCode': 200,
                    'body': json.dumps({
                        'isMacro': True,
                        'values': {
                            'MeanCurvature': None,
                            'MaxCurvature': None,
                            'MinCurvature': None,
                            'CurvatureStd': None
                        }
                    })
                }

        else:
            response = {
                'statusCode': 200,
                'body': json.dumps({
                    'isMacro': True,
                    'values': {
                        'MeanCurvature': None,
                        'MaxCurvature': None,
                        'MinCurvature': None,
                        'CurvatureStd': None
                    }
                })
            }

        # 결과 반환
        return response


    except Exception as e:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': str(e)}),
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            }
        }
